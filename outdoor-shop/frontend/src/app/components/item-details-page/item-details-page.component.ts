import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ItemService } from '../../services/items.service';
import { ActivatedRoute, Params } from '@angular/router';
import { switchMap } from 'rxjs';
import { ImageDto, ItemDefinition2 } from '../../services/models';
import { ToastrService } from 'ngx-toastr';
import { BasketService } from '../../services/basket.service';

@Component({
  selector: 'app-item-details-page',
  templateUrl: './item-details-page.component.html',
  styleUrl: './item-details-page.component.scss',
})
export class ItemDetailsPageComponent implements OnInit {
  items!: ItemDefinition2[];
  images!: ImageDto[];

  selectedSize?: string;
  selectedColor?: string;

  constructor(
    private itemService: ItemService,
    private route: ActivatedRoute,
    private toastrService: ToastrService,
    private basketService: BasketService,
    private cdr: ChangeDetectorRef
  ) {}

  addToBusket(): void {
    this.basketService.addItemToBasket({
      productId: this.getItemByColorAndSize().variation_id,
      quantity: 1,
    });
  }

  private getItemByColorAndSize(): ItemDefinition2 {
    return this.items.find(
      (item) =>
        item.size_option_name == this.selectedSize &&
        item.colour_name == this.selectedColor
    )!;
  }

  getSizes(): string[] {
    return Array.from(new Set(this.items.map((item) => item.size_option_name)));
  }

  getColors(): string[] {
    return Array.from(new Set(this.items.map((item) => item.colour_name)));
  }

  selectSize(size: string): void {
    if (this.selectedSize == size) {
      this.selectedSize = undefined;
      return;
    }
    this.selectedSize = size;
  }

  selectColor(color: string): void {
    if (this.selectedColor == color) {
      this.selectedColor = undefined;
      return;
    }
    this.selectedColor = color;
  }

  ngOnInit(): void {
    this.route.params
      .pipe(
        switchMap((params: Params) =>
          this.itemService.getDataById(+params['id'])
        )
      )
      .subscribe(
        (res) => {
          this.items = res;
          this.loadImagesById(this.items[0]!.product_id);
        },
        (error) => {
          this.toastrService.error(error.error.detail);
        }
      );
  }

  private loadImagesById(id: number): void {
    this.itemService.getImagesById(id).subscribe((images) => {
      this.images = images;
      this.cdr.detectChanges();
    });
  }
}
