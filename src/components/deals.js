import React, {Component} from "react";

class Deals extends Component{
    constructor(props) {
        super(props);
        this.state = {messages:[]};     // placeholder to hold deals data 
    }

    componentDidMount() {
        const source = new EventSource('http://localhost:8090/deals');


        source.addEventListener(
            'connected',
            event => {
                const message = JSON.parse(event.data);
                this.setState({
                    messages: [
                        ...this.state.messages,
                        {text: `Connected: ${message.data}`, date: null, id: 0},
                    ],
                });
            },
            false,
        );


        source.addEventListener(   // whenever a new message is received, state is updated
            'message',
            event => {                  
                const message = JSON.parse(event.data);
                console.log(message);
                this.setState({
                    messages: [
                        ...this.state.messages,
                        {
                            instrumentName: message.instrumentName,
                            type: message.type,
                            price: message.price,
                            id: this.state.messages.length + 1,
                        },
                    ],
                });
            },
            false,
        );
    }

    renderMessages() {
        return this.state.messages.map(message => (
            <tr key={message.id}>
                <td>{message.instrumentName}</td>
                <td>{message.price}</td>
                <td>{message.type}</td>
            </tr>
        ));
    }


    render() {                    // render function re rendered every time the state is updated
        return(
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>Instument Name</th>
                        <th>Price</th>
                        <th>Type</th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.renderMessages()}
                    </tbody>
                </table>
            </div>
        );

    }
}


export default Deals;