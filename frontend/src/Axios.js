import axios from 'axios';
console.log('Environment:', process.env.REACT_APP_NODE_ENV);
console.log('API URL:', process.env.REACT_APP_API_URL);

const { protocol, hostname } = window.location;
let baseURL = '';

baseURL = process.env.REACT_APP_API_URL;

const Axios = axios.create({
    baseURL: baseURL,
});

Axios.interceptors.response.use(
    response => {
        return response;
    },
    error => {
        if (!error.response) {
            console.warn("Network hatası veya server cevap vemedi:", error);
        }
        else if (error?.response?.status === 404) {
            console.warn("404 error", error);
        }
        return Promise.reject(error);
    }
);



export default Axios;
