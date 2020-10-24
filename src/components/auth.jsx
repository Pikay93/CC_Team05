import React, {Component} from "react";
import axios from 'axios';

class Auth extends Component{
    constructor(props) {
        super(props);
        this.state = {
            username:"",
            password:"",
            disabled : false
        };
    }

    handleSubmit = async (e, handleForUpdate) => {
        e.preventDefault();
        if (this.state.disabled) {
            return;
        }
        this.setState({disabled: true});
        console.log("Clicked", this.props.isLoggedIn);
        await axios.post('http://localhost:8090/login', {
            username: this.state.username,
            password: this.state.password
        })
            .then((response) => {
                if(response.data.isLoggedin){
                    alert("User Logged In");
                    handleForUpdate("something")
                }
                else{
                    alert("Please check your credentials and try again!");
                    this.setState({ disabled: false });
                }
            })
            .catch(error => { alert("Error Occurred");this.setState({ disabled: false });console.log(error); });
    };

    render() {
        const handleForUpdate = this.props.handleForUpdate;
        return(
            <div>
                <form>
                Username <input value={this.state.username}
                                placeholder={"username"}
                                type={"text"}
                                onChange={e => {this.setState({username:e.target.value});
                                            this.value= this.state.username}}/><br/>
                Password <input value={this.state.password}
                                placeholder={"password"}
                                type={"password"}
                                onChange={e => {this.setState({password:e.target.value});
                                    this.value= this.state.password}}/><br/>
                <button onClick={(e) => this.handleSubmit(e, handleForUpdate)} disabled={this.state.disabled}>{this.state.disabled ? 'Sending...' : 'Submit'}
                </button><br/>
                </form>
            </div>
        );
    }
}


export default Auth;