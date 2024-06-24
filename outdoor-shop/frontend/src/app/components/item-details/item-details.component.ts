import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  Input,
  OnInit,
} from '@angular/core';
import { ItemDefinition2 } from '../../services/models';
import { BasketService } from '../../services/basket.service';
import { ItemService } from '../../services/items.service';

@Component({
  selector: 'app-item-details',
  templateUrl: './item-details.component.html',
  styleUrl: './item-details.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ItemDetailsComponent implements OnInit {
  @Input() itemDef!: ItemDefinition2;

  constructor(
    private basketService: BasketService,
    private itemService: ItemService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.itemService
      .getImagesById(this.itemDef!.product_id)
      .subscribe((images) => {
        this.itemDef.image_url = images[0].image_url;
        this.cdr.detectChanges();
      });
  }

  addToBusket(): void {
    this.basketService.addItemToBasket({
      productId: this.itemDef!.variation_id,
      quantity: 1,
    });
  }
}
