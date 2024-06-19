import { ChangeDetectorRef, Component, inject, OnInit } from '@angular/core';
import { BasketService } from '../../services/basket.service';
import { BasketItem, ItemDefinition } from '../../services/models';
import { ItemService } from '../../services/items.service';
import { MatDialog } from '@angular/material/dialog';
import { BasketConfirmDialogComponent } from '../basket-confirm-dialog/basket-confirm-dialog.component';

@Component({
  selector: 'app-basket',
  templateUrl: './basket.component.html',
  styleUrl: './basket.component.scss',
})
export class BasketComponent implements OnInit {
  basketItems: BasketItem[] = [];
  itemDefinitions: ItemDefinition[] = [];

  private readonly dialog = inject(MatDialog);

  constructor(
    private basketService: BasketService,
    private itemService: ItemService,
    private cdr: ChangeDetectorRef
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

  deleteItem(id: number): void {
    this.basketService.removeItemFromBasket(id, 1);
  }

  openConfirmDialog(): void {
    const ref = this.dialog.open(BasketConfirmDialogComponent);
    ref.afterClosed().subscribe(() => {
      this.basketItems = this.basketService.getBasketItems();
      this.cdr.detectChanges();
    });
  }
}
