package com.mycompany.ukl_latihann;

import java.util.Scanner;

public class bayar_kuliah {
     public static void main(String[] args) {
     System.out.println("Seleksi Kondisi Pembayaran KULIAH!");
            Scanner kuliah = new Scanner(System.in);
            String ulang;
            String[] nama_user = {"Mira","Nina","Oemar","Pena"};
            String[] alamt = {"Sawojajar","Kedung Kandang","Ijen","Dinoyo"};
            int[] id_user = {1,2,3,4};
            String[] jalur = {"SBMPTN","SNMPTN","Mandiri"};
            String[] kat_gol = {"A","B","C"};
            String[] spp = {"500 Ribu","1 Juta","2 Juta","3 Juta"};
            do { System.out.print("Masukkan ID Anda : ");
            int ID = kuliah.nextInt();
            System.out.print("Masukkan Pendapatan Anda : ");
            int income = kuliah.nextInt();
            System.out.println("Jumlah SPP yang akan dibayar bulan ini : ");
            int SPP = kuliah.nextInt();
            switch (ID) {
                case 1: for (int i = 0; i < ID; i++) {
                    System.out.println("ID : "+id_user[i]);
                    System.out.println("Nama : "+nama_user[i]);
                    System.out.println("Jalur : "+jalur[i]);
                    System.out.println("Alamat : "+alamt[i]);
                    System.out.println("=================================");
                } if (income <2000000) {
                    System.out.println("Golongan : "+kat_gol[0]);
                    System.out.println("SPP yang harus dibayar adalah : "+spp[0]);
                    int hitung_spp = SPP-500000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } else if (income >=2000000 && income<=10000000) {
                    System.out.println("Golongan : "+kat_gol[1]);
                    System.out.println("SPP yang harus dibayar : "+spp[1]);
                    int hitung_spp = SPP-1000000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } else if (income >10000000) {
                    System.out.println("Golongan : "+kat_gol[2]);
                    System.out.println("SPP yang harus dibayar adalah : "+spp[2]);
                    int hitung_spp = SPP-2000000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } break;

                case 2: for (int i = 1; i < ID; i++) {
                    System.out.println("ID : "+id_user[i]);
                    System.out.println("Nama : "+nama_user[i]);
                    System.out.println("Jalur : "+jalur[i]);
                    System.out.println("Alamat : "+alamt[i]);
                    System.out.println("=================================");
                } if (income <2000000) {
                    System.out.println("Golongan : "+kat_gol[0]);
                    System.out.println("SPP yang harus dibayar adalah : "+spp[0]);
                    int hitung_spp = SPP-500000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } else if (income >=2000000 && income<=10000000) {
                    System.out.println("Golongan : "+kat_gol[1]);
                    System.out.println("SPP yang harus dibayar : "+spp[1]);
                    int hitung_spp = SPP-1000000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } else if (income >10000000) {
                    System.out.println("Golongan : "+kat_gol[2]);
                    System.out.println("SPP yang harus dibayar adalah : "+spp[2]);
                    int hitung_spp = SPP-2000000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } break;

                case 3: for (int i = 2; i < ID; i++) {
                    System.out.println("ID : "+id_user[i]);
                    System.out.println("Nama : "+nama_user[i]);
                    System.out.println("Jalur : "+jalur[i]);
                    System.out.println("Alamat : "+alamt[i]);
                    System.out.println("=================================");
                } if (income <2000000) {
                    System.out.println("Golongan : "+kat_gol[0]);
                    System.out.println("SPP yang harus dibayar adalah : "+spp[0]);
                    int hitung_spp = SPP-500000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } else if (income >=2000000 && income<=10000000) {
                    System.out.println("Golongan : "+kat_gol[1]);
                    System.out.println("SPP yang harus dibayar : "+spp[1]);
                    int hitung_spp = SPP-1000000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } else if (income >10000000) {
                    System.out.println("Golongan : "+kat_gol[2]);
                    System.out.println("SPP yang harus dibayar adalah : "+spp[3]);
                    int hitung_spp = SPP-3000000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } break;
                
                case 4: for (int i = 3; i < ID; i++) {
                    System.out.println("ID : "+id_user[i]);
                    System.out.println("Nama : "+nama_user[i]);
                    System.out.println("Jalur : "+jalur[i-3]);
                    System.out.println("Alamat : "+alamt[i]);
                    System.out.println("=================================");
                } if (income <2000000) {
                    System.out.println("Golongan : "+kat_gol[0]);
                    System.out.println("SPP yang harus dibayar adalah : "+spp[0]);
                    int hitung_spp = SPP-500000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } else if (income >=2000000 && income<=10000000) {
                    System.out.println("Golongan : "+kat_gol[1]);
                    System.out.println("SPP yang harus dibayar : "+spp[1]);
                    int hitung_spp = SPP-1000000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } else if (income >10000000) {
                    System.out.println("Golongan : "+kat_gol[2]);
                    System.out.println("SPP yang harus dibayar adalah : "+spp[2]);
                    int hitung_spp = SPP-2000000;
                    System.out.println("Sisa Bayaran anda : "+hitung_spp);
                } break;
            }
            System.out.println("============================================");
            System.out.print("Ulang? (y/n) : ");
            ulang = kuliah.next();
            } while (ulang.equalsIgnoreCase("y"));
            System.out.println("okai");

    }
}