import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-quantity-label',
  templateUrl: './quantity-label.component.html',
  styleUrl: './quantity-label.component.scss',
})
export class QuantityLabelComponent implements OnInit {
  @Input() quantity!: number;

  color = 'green';
  label = 'Na stanie';

  ngOnInit(): void {
    this.getItemQuantityLabel();
  }

  getItemQuantityLabel(): void {
    if (this.quantity < 1) {
      this.color = 'red';
      this.label = 'Brak';
    } else if (this.quantity < 5) {
      this.color = 'orange';
      this.label = 'Ostatnie sztuki';
    } else if (this.quantity < 15) {
      this.color = 'yellow';
      this.label = 'Mała ilość';
    } else {
      this.color = 'green';
      this.label = 'Na stanie';
    }
  }
}
