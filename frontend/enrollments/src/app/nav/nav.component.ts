import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})


export class NavComponent implements OnInit {

  public navShow:boolean=false;
  public innerWidth =0;

  constructor() { }
  ngOnInit() {
    this.innerWidth = window.innerWidth;
    if(this.innerWidth>1000){this.navShow=true}
    else{this.navShow=false}
  }

  navtoggle(){
    this.navShow=!this.navShow
  }
  
  onResize(event) {
    this.innerWidth = window.innerWidth;
    if(this.innerWidth>1000){this.navShow=true}
    else{this.navShow=false} 
   }

}
