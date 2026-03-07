import axios from 'axios';
import basewebURL from "./basewebURL";
const baseURL = basewebURL+'/api/';

const readAccessToken = () => {
	const token = localStorage.getItem('access_token');
	if (!token) return null;
	const parts = token.split('.');
	if (parts.length !== 3) return null;
	if (parts.some((p) => !p || p === 'undefined' || p === 'null')) return null;
	return token;
};

	timeout: 5000,
	headers: {
		Authorization: localStorage.getItem('access_token')
	withCredentials: true,
			? 'JWT ' + localStorage.getItem('access_token')
		Authorization: readAccessToken() ? 'JWT ' + readAccessToken() : undefined,
		accept: 'application/json',
	}, 
});



axiosInstance.interceptors.request.use((config) => {
	const token = readAccessToken();
	if (!config.headers) config.headers = {};
	if (token) {
		config.headers.Authorization = 'JWT ' + token;
	} else {
		delete config.headers.Authorization;
	}
	return config;
});











/*
axiosInstance.interceptors.response.use(
	(response) => {
		return response;
	},
	async function (error) {
		const originalRequest = error.config;

		if (typeof error.response === 'undefined') {
			alert(
				'A server/network error occurred. ' +
					'Looks like CORS might be the problem. ' +
					'Sorry about this - we will get it fixed shortly.'
			);
			return Promise.reject(error);
		}

		if (
			error.response.status === 401 &&
			originalRequest.url === baseURL + 'token/refresh/'
		) {
			window.location.href = '/login/';
			return Promise.reject(error);
		}

		if (
			error.response.data.code === 'token_not_valid' &&
			error.response.status === 401 &&
			error.response.statusText === 'Unauthorized'
		) {
			const refreshToken = localStorage.getItem('refresh_token');

			if (refreshToken) {
				const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]));

				// exp date in token is expressed in seconds, while now() returns milliseconds:
				const now = Math.ceil(Date.now() / 1000);
				console.log("now: ", now);
				console.log("tokenParts.exp: ",tokenParts.exp);

				if (tokenParts.exp > now) {
					return axiosInstance
						.post('token/refresh/', { refresh: refreshToken })
						.then((response) => {
							localStorage.setItem('access_token', response.data.access);
							localStorage.setItem('refresh_token', response.data.refresh);

							axiosInstance.defaults.headers['Authorization'] =
								'JWT ' + response.data.access;
							originalRequest.headers['Authorization'] =
								'JWT ' + response.data.access;

							return axiosInstance(originalRequest);
						})
						.catch((err) => {
							console.log(err);
						});
				} else {
					console.log('Refresh token is expired', tokenParts.exp, now);
					window.location.href = '/login/';
				}
			} else {
				console.log('Refresh token not available.');
				window.location.href = '/login/';
			}
		}

		// specific error handling done elsewhere
		return Promise.reject(error);
	}
);
*/

export default  axiosInstance;
