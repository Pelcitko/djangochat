import React from "react";
import { NavLink } from "react-router-dom";

const Contact = props => (
  <NavLink to={`${props.chatURL}`} style={{ color: "#fff" }}>
    <li className="contact">
      <div className="wrap">
        <span className="contact-status active" />
        <img src={props.picURL} alt={`profile of ${props.name}`} />
        <div className="meta">
          <p className="name">{props.name}</p>
           <p className="preview">{props.messages}</p>
        </div>
      </div>
    </li>
  </NavLink>
);

export default Contact;
