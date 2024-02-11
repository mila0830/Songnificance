import React, { useState } from "react";
import {useNavigate, useLocation} from "react-router-dom";
import "./Home.css"
import axios from "axios";

function sayHello() {
  alert('You clicked me!');
}


function Home() {
    const navigate = useNavigate();
  const [songTerm, setSongTerm] = useState('');
  const [artistTerm, setArtistTerm] = useState('');
  const [responseSong, setResponseSong] = useState('');
  const [responseArtist, setResponseArtist] = useState('');
  const [responseSummary, setResponseSummary] = useState('');

  

  const handleSearch = async (e) => {
    
    e.preventDefault();
    // Example API endpoint (replace with your actual endpoint)
    //is this correct? I think I should adjust this but not sure with what
    const apiUrl = "http://localhost:8000/results"
    console.log("hey")
    
    try {
      const formData = new FormData();
      formData.append("song", songTerm);
      formData.append("artist", artistTerm);
     
      //using a post method type
      const response = await axios.post(apiUrl, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      // Handle the response as needed
      console.log("API Response:", response.data);
      setResponseSong(response.data.song);
      setResponseArtist(response.data.artist);
      setResponseSummary(response.data.summary);

      //navigate('/results');
    } catch (error) {
      // Handle errors
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.error("Response data:", error.response.data);
        console.error("Response status:", error.response.status);
        console.error("Response headers:", error.response.headers);
      } else if (error.request) {
        // The request was made but no response was received
        console.error("No response received:", error.request);
      } else {
        // Something happened in setting up the request that triggered an Error
        console.error("Request setup error:", error.message);
      }
      console.error("API Request Error:", error);
    }
  };

  return (
    <div className="home">
      <div className="container">
        {
        !responseSong&& 
        <>
        <h1 className="title">Songnificance</h1>
        <h2 className="second-header">Uncover the story behind your favorite song with just one click!</h2>
        <div className="row align-items-center my-5">
          <div className="col-lg-7">
            <input
              type="text"
              placeholder="Enter song name"
              value={songTerm}
              onChange={(e) => setSongTerm(e.target.value)}
            />
            <input
              type="text"
              placeholder="Enter artist name"
              value={artistTerm}
              onChange={(e) => setArtistTerm(e.target.value)}
              
            />
            <button onClick={handleSearch}>Search</button>
        
          </div>
          <div className="col-lg-5"></div>
        
        </div>
        </>
        }
        {
            responseSong&&
            <>
            <div>
            <h1 className="title-two">The Meaning</h1>
            <h2 className="body-text">{responseSummary}</h2>
            <h2 className="corner-text"> SONGNIFICANCE </h2>
            </div>
            </>
        }

      </div>

    </div>
  );
}

export default Home;