import { Component, OnInit } from '@angular/core';
import {HttpService} from './http.service';
import { createHash } from 'crypto';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})


export class AppComponent implements OnInit{
  
  public nano = new Map();
  public x=5;
  public name ="mohannad";
  public degrees;
  public degreesToPresent=[];
  public search=0;
  public searchPhrase:string='';
  public filterShow=false;
  public innerWidth =0;
  public userID=123456;
  // public search:any = '';
 
  constructor(private _http: HttpService){
  }

  filterShowOrNot(){
    this.innerWidth = window.innerWidth;
    if(this.innerWidth>1000){this.filterShow=true}
  }

  loadNanos(){
    this.name="Allah"
    console.log("YA RAB")
    this._http.getNanos().subscribe(data => {
      this.degrees=data['degrees'];
      //console.log(this.degrees)
      this.degrees.forEach(element => {
        if(element["available"]==true && element["open_for_enrollment"]==true){
          this.degreesToPresent.push(element)
          console.log(element["title"]) 
        }
        
      });
    });
  }

  ngOnInit(){
    this.filterShowOrNot();
    this.loadNanos();
  }

 
  onResize(event) {
    this.innerWidth = window.innerWidth;
    if(this.innerWidth>1000){this.filterShow=true}
    else{this.filterShow=false} 
   }

   enrole(name:string){ 
    let reqBody={
      "nanodegree_key": name,
      "udacity_user_key": this.userID
      //"enrollment_id": createHash(name+this.userID)
    }
    //console.log(reqBody)
    this._http.postENrole(reqBody).subscribe(data => {
      alert(data["state"])
    })
  }
}
