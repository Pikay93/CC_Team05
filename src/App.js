import React, {Component} from 'react';
import Deals from "./components/deals";
import Auth from "./components/auth";
import CheckDB from "./components/checkDatabase"


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {isLoggedIn:false};
    }

    handleForUpdate(someArg){
        this.setState({isLoggedIn:true});
    }

    render(){
        let handleForUpdate =   this.handleForUpdate;
        return (
            <div>
                {<CheckDB/>}<br/>
                {this.state.isLoggedIn ? <Deals /> : <Auth handleForUpdate = {handleForUpdate.bind(this)}/>  }
            </div>
        );
    }
}
export default App;
