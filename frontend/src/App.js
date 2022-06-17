import React, {Component} from "react"
import axios from 'axios'
import {BarElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, Title, Tooltip,} from 'chart.js'
import {Bar} from 'react-chartjs-2'

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            orderList: []
        }
    }

    async componentDidMount() {
        try {
            const response = await axios.get('http://0.0.0.0:8000/api/v1/orders/')
            return this.setState({
                orderList: response.data
            })

        } catch (e) {
            console.log(e);
        }
    }

    chart() {

        const dates = this.state.orderList.map(order => order.delivery_date.slice(0, 10))
        const prices_rub = this.state.orderList.map(order => order.price_rub)

        return {
            labels: dates,
            datasets: [
                {
                    label: 'Price RUB',
                    data: prices_rub,
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                }
            ]
        }
    }

    total() {
        const prices_rub = this.state.orderList.map(order => parseFloat(order.price_rub))
        return prices_rub.reduce((a, b) => a + b, 0)
    }

    render() {
        return (

            <main>
                <Bar
                    data={this.chart()}
                    height={"90%"}
                    options={{
                        responsive: true,
                        plugins: {
                            title: {
                                display: true,
                                text: 'Стоимость заказов в рублях',
                            },
                        }
                    }}
                />
                <div><h3>Общая стоимость {this.total().toFixed(2)} руб.</h3></div>
            </main>


        )
    }
}

export default App;
