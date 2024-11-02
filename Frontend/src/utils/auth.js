import {useAuthStore} from "../store/ath";
import axios from "./axios";
import jwt_decode from "jwt-decode";
import Cookie from "js-cookie";
import Swal from "sweetalert2";

export const login = async (email, password) => {
    try{
        const { data, status } = await axios.post(`user/token/`, {
            email,
            password
        });
        
        if(status === 200){
            setAuthUser(data.accesss, data.refresh);
            alert("Login Successful");
        }
        return {data, error: null};

    } catch (error){
        return {
            data: null,
            error: error.response.data?.detail || "Something went wrong",
        }
    }
};