import { ChangeDetectorRef, Component, Inject, OnInit } from '@angular/core';
import { BasketItem, ItemDefinition2 } from '../../services/models';
import { BasketService } from '../../services/basket.service';
import { ItemService } from '../../services/items.service';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-basket-confirm-dialog',
  templateUrl: './basket-confirm-dialog.component.html',
  styleUrl: './basket-confirm-dialog.component.scss',
})
export class BasketConfirmDialogComponent {
  constructor(
    private basketService: BasketService,
    private itemService: ItemService,
    private cdr: ChangeDetectorRef,
    public dialogRef: MatDialogRef<BasketConfirmDialogComponent>,
    private toastrService: ToastrService,
    @Inject(MAT_DIALOG_DATA)
    public data: {
      itemDefinitions: ItemDefinition2[];
      basketItems: BasketItem[];
    }
  ) {}

  getItemDefById(id: number): ItemDefinition2 | undefined {
    return this.data.itemDefinitions
      .filter((item) => item.variation_id === id)
      .at(0);
  }

  buyItems(): void {
    for (const [index, item] of this.data.basketItems.entries()) {
      this.itemService.buyItems(item).subscribe(
        (response) => {
          if (index == this.data.basketItems.length - 1) {
            this.toastrService.success('Products bought successfully!');
            this.dialogRef.close();
          }
          this.basketService.removeItemFromBasket(
            item.productId,
            item.quantity
          );
        },
        (error) => {
          this.toastrService.error(error.error.detail);
        }
      );
    }
  }
}
