import React, {Component} from "react"
import axios from 'axios';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            orderList: []
        };
    }

    componentDidMount() {
        try {
            axios.get('http://0.0.0.0:8000/api/v1/orders/').then(response => this.setState({
                orderList: response.data
            }))

        } catch (e) {
            console.log(e);
        }
    }

    renderOrders = () => {

        return this.state.orderList.map(order => (
            <li
                key={order.order_id}
                className="list-group-item d-flex justify-content-between align-items-center"
            >
                <span>{order.price_s}</span>
                <span>{order.price_rub}</span>
                <span>{order.delivery_date}</span>
            </li>
        ));
    };

    render() {
        return (
            <main className="content">
                <div className="row">
                    <div className="col-md-6 col-sm-10 mx-auto p-0">
                        <div className="card p-3">
                            <ul className="list-group list-group-flush">
                                {this.renderOrders()}
                            </ul>
                        </div>
                    </div>
                </div>
            </main>
        )
    }
}

export default App;
