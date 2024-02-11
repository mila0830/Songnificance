import React, { useState, useEffect } from "react";
import axios from "axios";

function Results(){
    const [summary, setSummary] = useState(null);

    useEffect(() => {

        // Fetch the summary data from your API
        axios.post("http://localhost:8000/results")
        
            .then(response => {
                console.log(response.data);
                setSummary(response.data);
                
            })
            .catch(error => {
                console.error("Error fetching summary:", error);
            });
    }, []);  // Empty dependency array to trigger the effect only once

    if (!summary) {
        return <div>Loading...</div>;
    }

    // Continue rendering your component with the summary data
    return (
        <div>
            <h2>Results Page</h2>
            <p>Song: {summary.song}</p>
            <p>Artist: {summary.artist}</p>
            <p>Summary: {summary.summary}</p>
            <div>
                {/* Render additional details from the summary object as needed */}
            </div>
        </div>
    );

}
export default Results