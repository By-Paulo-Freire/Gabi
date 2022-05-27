import React from 'react';
import ReactDOM from 'react-dom';
import Mouth from './Mouth';
import './head.css';

class Head extends React.Component {
  render () {
    return (
    <div class="gabi">
    <div class="bg-hair">
      <div class="head">
        <div class="eye radius ha hb"></div>
        <div class="eye radius ha hb"></div>
        <div class="nose"></div>
        <div class="eyebrow"></div>
        <div class="eyebrow"></div>
        <Mouth />
        <div class="fg-hair"></div>
      </div>
    </div>
  </div>

    );
  }
}

export default Head;