import React from "react";
import './App.css';
import AuthorList from "./components/Author";
import axios from "axios";
import Grid from '@material-ui/core/Grid';
import UserList from "./components/User";
import Header from "./components/layout/Header";
import Footer from "./components/layout/Footer";


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
        'users': [],
    }
  }

  componentDidMount() {
      axios.get('http://127.0.0.1:8000/api/users')
          .then(resonse => {
              const users = resonse.data
                this.setState(
                    {
                        'users': users
                    }
                )
          }).catch(error => console.log(error))
  }

  render() {
    return (
        <div>
            <Header />
            <UserList users={this.state.users}/>
            <Footer />
        </div>

    )
  }
}
export default App;