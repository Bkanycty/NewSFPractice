import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class PostService{

    getPosts() {
        const url = `${API_URL}/api/news/`;
        return axios.get(url).then(response => response.data);
    }

    setLikePost(id) {
        const url = `${API_URL}/api/like_post/` + id;
        return axios.get(url).then(response => response.data);
    }

    deletePost(id) {
        const url = `${API_URL}/api/news/` + id;
        return axios.delete(url, {data: {post_id: id}}).then(response => response.data);
        }

    createPost(text){
        const url = `${API_URL}/api/news/`;
        return axios.post(url,text);
    }
}