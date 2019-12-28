import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { }

  getNanos() {
    return this.http.get('https://catalog-api.udacity.com/v1/degrees')
  }
  postENrole(req:any) {
    return this.http.post('http://localhost:5000/enrollments',req)
  }
}