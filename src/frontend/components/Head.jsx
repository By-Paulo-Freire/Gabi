import React from 'react';
import Mouth from './Mouth';
import Nose from './Nose';
import Eye from './Eyes';
import Eyebrows from './Eyebrow';
import './head.css';

class Head extends React.Component {
  render () {
    return (
    <div class="gabi">
    <div class="bg-hair">
      <div class="head">
        <div class="fg-hair"></div>
        <Eye />
        <Eye />
        <Eyebrows />
        <Eyebrows />
        <Nose />
        <Mouth />
      </div>
    </div>
  </div>

    );
  }
}

export default Head;