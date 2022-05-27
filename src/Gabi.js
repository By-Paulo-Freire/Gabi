import React from 'react';
import Head from './components/Head';


class Gabi extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          emotion: 'teste',
        };
      }
    render () {
        return (
            <Head />
        )
    }
}

export default Gabi;