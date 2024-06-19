import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ItemService } from '../../services/items.service';
import { ItemDefinition, ItemStock } from '../../services/models';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.scss',
})
export class AdminComponent implements OnInit {
  itemDefs: ItemDefinition[] = [];
  itemStock: ItemStock[] = [];

  displayedColumns: string[] = ['id', 'productId', 'productName', 'quantity'];

  constructor(
    private authService: AuthService,
    private router: Router,
    private toastr: ToastrService,
    private itemService: ItemService
  ) {}

  ngOnInit(): void {
    this.itemService.getItemDefinitions().subscribe((defs) => {
      this.itemDefs = defs;
    });

    this.itemService.getItemsStock().subscribe((stock) => {
      this.itemStock = stock;
    });
  }

  getItemDefById(id: number): ItemDefinition | undefined {
    return this.itemDefs.filter((item) => item.id === id).at(0);
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['']);
    this.toastr.success('Logged out successfully!');
  }
}
