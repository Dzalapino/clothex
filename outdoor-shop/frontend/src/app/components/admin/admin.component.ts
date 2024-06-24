import { Component, inject, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ItemService } from '../../services/items.service';
import { ItemDefinition2, ItemStock } from '../../services/models';
import { MatDialog } from '@angular/material/dialog';
import { RequestNeedDialogComponent } from '../request-need-dialog/request-need-dialog.component';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.scss',
})
export class AdminComponent implements OnInit {
  itemDefs: ItemDefinition2[] = [];
  itemStock: ItemStock[] = [];

  displayedColumns: string[] = [
    'id',
    'productId',
    'productName',
    'color',
    'size',
    'quantity',
    'actions',
  ];

  private readonly dialog = inject(MatDialog);

  constructor(
    private authService: AuthService,
    private router: Router,
    private toastr: ToastrService,
    private itemService: ItemService
  ) {}

  ngOnInit(): void {
    this.itemService.getData().subscribe((defs) => {
      this.itemDefs = defs.flat();
    });

    this.itemService.getItemsStock().subscribe((stock) => {
      this.itemStock = stock;
    });
  }

  getItemStockById(variation_id: number): ItemStock | undefined {
    return this.itemStock
      .filter((item) => item.productId == variation_id)
      .at(0);
  }

  openDialog(name: string, id: number): void {
    const ref = this.dialog.open(RequestNeedDialogComponent, {
      data: { name, id },
    });
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['']);
    this.toastr.success('Logged out successfully!');
  }
}
