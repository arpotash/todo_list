import React from 'react';
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import {BrowserRouter, Link, Route} from "react-router-dom";

const MainMenu = () => {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const preventDefault = (event) => event.preventDefault();
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
      <div>
          <BrowserRouter>
              <nav>
                  <ul>
                      <li><Link to='/users'>Users</Link></li>
                      <li>Projects</li>
                      <li>Notes</li>
                  </ul>
              </nav>
          </BrowserRouter>
      </div>
  )
}

export default MainMenu;
