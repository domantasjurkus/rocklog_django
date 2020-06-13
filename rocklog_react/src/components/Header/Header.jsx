import React from 'react';

const Header = () => (
  <div style="background: url({% static 'rocklog/img/bg_darken.jpg' %})"
  class="section no-pad-bot parallax-container background responsive-img" id="index-banner">
  <div class="container">
    <br />
    <br />
    <h1 class="header center">
      <a class="red-text text-shadow text-accent-4" href="/">RockLog</a>
    </h1>
    <div class="row center">
      <h5 class="header col s12 light white-text text-shadow">Naujausios dainos iš
        <a class="red-text" href="https://rockfm.lt/">ROCK FM</a>
      </h5>
    </div>
    <br />
    <br />
  </div>
</div>
);

export default Header;
