import React from "react";
import styled from 'styled-components';

const Eyebrow = styled.div`
    & {
        width: 36%;
        height: 20%;
        border-radius: 0 30% 0 0;
        box-shadow: -0.75vmin -3vmin 0 -1vmin var(--hair);
        top: 33%;
        left: 55%;
    }
    & + .Eyebrow {
        border-radius: 30% 0 0 0;
        box-shadow: 0.75vmin -3vmin 0 -1vmin var(--hair);
        left: 5%;
    }
`;

class Eyebrows extends React.Component {
    render() {
        return (
            <Eyebrow className="Eyebrow"/>
        );
    }
}

export default Eyebrows;