import {useState, useEffect} from 'react'
import axios from "axios"
export default function useAuth(code){
    const [accessToken, setAccessToken] = useState()
    const [refreshToken, setRefreshToken] = useState()
    const [expiresIn, setExpiresIn] = useState()

    useEffect(() => {
        console.log('Code:', code);
        fetch('http://localhost:3002/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code }),
        })
        .then((response) => {
        console.log('Response:', response);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setAccessToken(data.accessToken);
        setRefreshToken(data.refreshToken);
        setExpiresIn(data.expiresIn);
        window.history.pushState({}, null, '/');
      })
      .catch((error) => {
        console.error('Login request failed:', error);
      });
      }, [code])
    

    useEffect(() => {
        if (!refreshToken || !expiresIn) return
        const interval = setInterval(() => {
            fetch('http://localhost:3002/refresh', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refreshToken }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          setAccessToken(data.accessToken);
          setExpiresIn(data.expiresIn);
        })
        .catch((error) => {
          console.error('Refresh request failed:', error);
          // window.location = "/"
        });
    }, (expiresIn - 60) * 1000);
        return () => clearInterval(interval);
    }, [refreshToken, expiresIn]);

    return accessToken
    }
