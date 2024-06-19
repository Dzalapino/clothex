import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { BasketItem, ItemDefinition } from '../../services/models';
import { BasketService } from '../../services/basket.service';
import { ItemService } from '../../services/items.service';
import { MatDialogRef } from '@angular/material/dialog';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-basket-confirm-dialog',
  templateUrl: './basket-confirm-dialog.component.html',
  styleUrl: './basket-confirm-dialog.component.scss',
})
export class BasketConfirmDialogComponent implements OnInit {
  basketItems: BasketItem[] = [];
  itemDefinitions: ItemDefinition[] = [];

  constructor(
    private basketService: BasketService,
    private itemService: ItemService,
    private cdr: ChangeDetectorRef,
    public dialogRef: MatDialogRef<BasketConfirmDialogComponent>,
    private toastrService: ToastrService
  ) {}

  ngOnInit(): void {
    this.basketItems = this.basketService.getBasketItems();
    this.itemService.getItemDefinitions().subscribe((items) => {
      this.itemDefinitions = items;
      this.cdr.detectChanges();
    });
  }

  getItemDefById(id: number): ItemDefinition | undefined {
    return this.itemDefinitions.filter((item) => item.id === id).at(0);
  }

  buyItems(): void {
    for (let item of this.basketItems) {
      this.itemService.buyItems(item).subscribe((response) => {
        if (response.startsWith('ERR:')) {
          this.toastrService.error('Error: ' + response.slice(4));
        } else {
          this.basketService.removeItemFromBasket(
            item.productId,
            item.quantity
          );
        }
      });
    }
    this.dialogRef.close();
  }
}
