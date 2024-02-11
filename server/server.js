const express = require('express');
const cors = require("cors")
const bodyParser = require("body-parser")
const SpotifyWebApi = require('spotify-web-api-node');

const app = express();
app.use(bodyParser.json())

const corsOptions = {
    origin: 'http://localhost:3001', // Replace with your React app's origin
    credentials: true, // Enable credentials (if needed)
  };
  
app.use(cors(corsOptions));

app.post('/refresh', async (req, res) => {
    
    const refreshToken = req.body.refreshToken;
    const spotifyApi = new SpotifyWebApi({
        redirectUri: 'http://localhost:3001/',
        clientId: '21c6a793a5af4788807fa3719bd47e41',
        clientSecret: '573cd4a34e2c4b5681f8093223976d5c',
        refreshToken,
    })
    spotifyApi
    .refreshAccessToken()
    .then((data) => {
        res.json({
            accessToken: data.body.accessToken,
            expiresIn: data.body.expiresIn,
        })
        
    })
    .catch(() => {
        
      res.sendStatus(400)
    })
})
app.post('/login', async (req, res) => {
    const code = req.body.code;
    const SpotifyApi = new SpotifyWebApi({
        redirectUri: 'http://localhost:3001',
        clientId: '21c6a793a5af4788807fa3719bd47e41',
        clientSecret: '573cd4a34e2c4b5681f8093223976d5c',
    })

    SpotifyApi
    .authorizationCodeGrant(code)
    .then(data => {
        res.json({
            accessToken: data.body.access_token,
            refreshToken: data.body.refresh_token,
            expiresIn : data.body.expires_in,
        })
    })
    .catch((error)=>{
        //console.log(error)
        res.sendStatus(400)
    })
})

app.listen(3002, () => {
    console.log('Server is running on port 3002');
  });