// eslint-disable-next-line no-unused-vars
import React, { Component } from 'react';
import { render } from 'react-dom';

import Header from '../Header/Header.jsx';
import Body from '../Body/Body.jsx';
import Footer from '../Footer/Footer.jsx';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: 'Loading',
    };
  }

  render() {
    return <>
      <Header />
      <Body />
      <Footer />
    </>;
  }
}

export default App;

const container = document.getElementById('app');
render(<App />, container);
