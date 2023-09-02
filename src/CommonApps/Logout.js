import axiosInstance from '../axios';
//import basewebURL from "../basewebURL";

export const Logout =()=>{

  const response = axiosInstance.post('logout/blacklist/', {
                        refresh_token: localStorage.getItem('refresh_token'),
                });
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
	        localStorage.removeItem('preferredCourseId');
                axiosInstance.defaults.headers['Authorization'] = null;
                window.location.replace( "https://dicelpip.com");


}
