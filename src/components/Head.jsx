import React from 'react';
import Mouth from './Mouth';
import Nose from './Nose';
import './head.css';

class Head extends React.Component {
  render () {
    return (
    <div class="gabi">
    <div class="bg-hair">
      <div class="head">
        <div class="fg-hair"></div>
        <div class="eye radius ha hb"></div>
        <div class="eye radius ha hb"></div>
        <div class="eyebrow"></div>
        <div class="eyebrow"></div>
        <Nose />
        <Mouth />
      </div>
    </div>
  </div>

    );
  }
}

export default Head;