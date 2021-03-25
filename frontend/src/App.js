import React from "react";
import './App.css';
import axios from "axios";
import UserList from "./components/User";
import Footer from "./components/layout/Footer";
import ProjectList from "./components/Project";
import NoteList from "./components/Note";
import {BrowserRouter, Route, Switch, Link, Redirect} from 'react-router-dom';
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import 'bootstrap/dist/css/bootstrap.min.css';
import {Nav, NavDropdown, Navbar, NavbarBrand} from "react-bootstrap";
import notfound_404 from './notfound_404.jpg';
import {makeStyles} from "@material-ui/core/styles";

const useStyles = makeStyles(
    {
        root: {
            'width': '60%',
            'height': '60%'
        },
        link: {
            'textDecoration': 'none',
            'color': '#000'
        }
    }
)

const NotFound404 = () => {
    const classes = useStyles();
    return (
        <img src={notfound_404} className={classes.root}/>
    )
}

class App extends React.Component {
  constructor(props) {
      super(props)
      this.state = {
          'users': [],
          'projects': [],
          'notes': []
      }
  }

  componentDidMount() {
      axios.get('http://127.0.0.1:8000/api/projects')
          .then(response => {
              const projects = response.data
                this.setState({projects: projects.results}
                )
          }).catch(error => console.log(error))
      axios.get('http://127.0.0.1:8000/api/users')
          .then(response => {
              const users = response.data
                this.setState({users: users})
          }).catch(error => console.log(error))

      axios.get('http://127.0.0.1:8000/api/notes')
          .then(response => {
              const notes = response.data
              console.log(notes)
                this.setState({notes: notes.results})
          }).catch(error => console.log(error))
  }

  render() {
      return (
        <div className="App">
            <BrowserRouter>
                    <div>
                      <AppBar position="static">
                        <Toolbar variant="dense">
                          <IconButton edge="start" color="inherit" aria-label="menu">
                            <MenuIcon />
                          </IconButton>
                            <Navbar collapseOnSelect="lg" bg="light" variant="light">
                                <Navbar.Brand>Home</Navbar.Brand>
                                <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
                                <Navbar.Collapse id="responsive-navbar-nav">
                                    <Nav className="mr-auto">
                                        <Nav.Link><Link to='/users'>Users</Link></Nav.Link>
                                        <Nav.Link><Link to='/projects'>Projects</Link></Nav.Link>
                                        <Nav.Link><Link to='/notes'>Notes</Link></Nav.Link>
                                    </Nav>
                                </Navbar.Collapse>
                            </Navbar>
                        </Toolbar>
                      </AppBar>
                    </div>
                <Switch>
                    <Route exact path='/users' component={() => <UserList users={this.state.users} />}  />
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />}  />
                    <Route exact path='/notes' component={() => <NoteList notes={this.state.notes} />}  />
                    <Redirect from='/' to='/notes' />
                    <Route component={NotFound404} />
                </Switch>
            </BrowserRouter>
            <Footer />
        </div>

    )
  }
}
export default App;