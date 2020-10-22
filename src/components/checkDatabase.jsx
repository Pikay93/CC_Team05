import React from "react";
import axios from 'axios';

class CheckDB extends React.Component {
    constructor(props) {
        super(props);
        this.state = {status: ""};
    }

    handleClick =  async () => {
        axios.get("http://localhost:8090/isDbRunning")
            .then(response => { this.setState({ status: response.data.isDatabaseUp }) })
            .catch(error => { alert("Error Occurred"); console.log(error); });
    };

    render() {

        return (
            <div>
                {this.state.status === "" ? null : this.state.status ? <h4>{'DB is Up'}</h4> : <h4>{'Db not running'}</h4>}
                <button type='button' onClick={this.handleClick}>Check</button>
            </div>
        );
    }
}

export default CheckDB;