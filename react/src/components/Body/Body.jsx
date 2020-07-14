import React from 'react';

const Body = () => (
  <>
    <div class=" row grey darken-4" style={{ 'min-height': '500px' }}>
      <div class="col s12 m10 l5 offset-m1 offset-l1">
          <br />
          <ul class="collapsible grey darken-4" data-collapsible="accordion">
              {/* <ul class="collection">
                  <li class="collection-item grey darken-3 grey-text">
                      {% if user.is_authenticated %}
                          <p style="float: left;">{{ user.first_name }}</p>
                          <p class="center-align">
                              <a href="{{ header_link_url }}">{{ header_link_text }}</a>
                              <a href="{% url 'rocklog:logout' %}" class="secondary-content">
                                  <i class="material-icons grey-text logout-icon">input</i>
                              </a>
                          </p>
                      {% else %}
                          <p class="grey-text">&nbspPrisijunk su <a href="{% url 'social:begin' 'google-oauth2' %}">Google</a> ir išsaugok dainas!</p>
                      {% endif %}
                  </li>
              </ul> */}
              <br />
              {/* {% for stream_entry in stream %}
                  <li>
                      <div class="song collapsible-header red darken-4 white-text">
                          <span>{{ stream_entry.playtime }}</span>
                          &nbsp
                          <b class="artist">{{ stream_entry.song.artist }}</b> -
                          <span class="song">{{ stream_entry.song.song }}</span>
                          <a href="javascript:;" class="secondary-content" id="{{ stream_entry.song.id }}">
                              {% if stream_entry.saved %}
                                  <i class="material-icons star-icon stared">grade</i>
                              {% else %}
                                  <i class="material-icons star-icon">grade</i>
                              {% endif %}
                          </a>
                      </div>
                      <div class="collapsible-body grey darken-4">
                          <div class="video-container" id="video-container"></div>
                      </div>
                  </li>
              {% endfor %}
              {% if stream|length == 0 %}
                  <ul class="collection">
                      <li class="collection-item grey darken-3 grey-text">
                          <p class="grey-text">Nėra išsaugotų dainų</p>
                      </li>
                  </ul>
              {% endif %} */}

          </ul>
      </div>
    </div>

    <div id="player"></div>

  </>
);

export default Body;
