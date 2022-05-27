import React from "react";
import ReactDOM from "react-dom";

class Nose extends React.Component {
    render() {
        return (
            <div style={nose}></div>
        );
    }
}

const nose = {
    width:' 16%',
    height: '30%',
    borderRadius: '0 0 5vmin 5vmin',
    border: '1vmin solid #0002',
    borderRight: '0.75vmin solid #0002',
    borderLeftColor: 'transparent',
    borderTop: '0',
    left: '50%',
    top: '43%',
    transform: 'translate(-70%, 0)',
}

export default Nose