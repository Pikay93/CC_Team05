import React, {Component} from "react";

class Deals extends Component{
    constructor(props) {
        super(props);
        this.state = {messages: [], isStreaming:true, buttonText:"Stop"};
        this.source = null;
    }

    startEventSource() {
        this.source = new EventSource('http://localhost:8090/deals');
        this.source.addEventListener(
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


        this.source.addEventListener(
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

    componentDidMount() {
        this.startEventSource();
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


    render() {
        return(
            <div>
                <button onClick={()=>{
                    if (this.state.isStreaming){
                        this.source.close();
                        this.setState({isStreaming:false, messages:[], buttonText:"Start"});
                    }
                    else{
                        this.setState({isStreaming:true, messages:[], buttonText:"Stop"});
                        this.startEventSource();
                    }

                }}>{this.state.buttonText}</button>
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