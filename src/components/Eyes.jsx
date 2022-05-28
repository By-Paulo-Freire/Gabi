import React from "react";
import styled from 'styled-components';

const Eyes = styled.div`
    & {
    width: 30%;
    height: 15%;
    background: #fff;
    top: 35%;
    left: 12%;
    box-shadow: inset 0 4vmin 0 -3vmin rgba(0,0,0,0.1),
    inset 0 4vmin 0 -3vmin var(--skin),
    0 -3vmin 3vmin -1vmin rgba(0,0,0,0.05);
    border-radius: 100%;
    }
    &:before {
        width: 4.2vmin;
        height: 3.7vmin;
        background: #222;
        border-radius: 50%;
        top: 55%;
        left: 50%; 
        transform: translate(-50%, -50%);
        box-shadow: 0 0 0 0.70vmin var(--iris);
    }
    &:after {
        width: 0.6vmin;
        height: 0.9vmin;
        background: #fff;
        border-radius: 100%;
        top: 35%;
        left: 59%;
    }
    & + .Eyes {
        left: 58%
    }
`;

class Eye extends React.Component {
    render() {
        return (
            <Eyes className="Eyes hb"/>
        );
    }
}

export default Eye;