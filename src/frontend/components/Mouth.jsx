import React from 'react';

class Mouth extends React.Component {
    render() {
        return (
            <div style={mouthHappy}></div>
        );
    }
}

const mouthHappy = {
    width: '35%',
    height: '8%',
    top: '80%',
    left: '50%',
    transform: 'translate(-50%, 0)',
    background: 'var(--skin)',
    borderRadius: '50% / 0% 0% 100% 100%',
    boxShadow: 'inset 0 0 0 2vmin rgba(128, 0, 0, 0.4)',
};

export default Mouth;