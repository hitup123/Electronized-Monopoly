import React from "react";
import Properties from "../Macros";

function Property({ propertyname }) {
    var propcolor = Properties[propertyname];

    const propplate = {
        backgroundColor: propcolor,
        color: 'white',
        display: 'inline-block',
        fontSize: '10px',
        padding: '5px', // Added padding for better appearance
        borderRadius: '10px', // Added border radius for better appearance
        fontWeight: '600',
        height: 'fit-content'
    }

    return (
        <p style={propplate}>{propertyname}</p>
    )
}

export default Property;
