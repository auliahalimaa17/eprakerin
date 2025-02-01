-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2025 at 01:59 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbprakerin`
--

-- --------------------------------------------------------

--
-- Table structure for table `berkas_peserta`
--

CREATE TABLE `berkas_peserta` (
  `id` int(11) NOT NULL,
  `id_peserta` int(11) NOT NULL,
  `surat_pengantar_magang` varchar(255) NOT NULL,
  `proposal_magang` varchar(255) NOT NULL,
  `curriculum_vitae` varchar(255) NOT NULL,
  `surat_pembuatan_idcard` varchar(255) DEFAULT NULL,
  `surat_penerimaan` varchar(255) DEFAULT NULL,
  `pas_foto` varchar(255) DEFAULT NULL,
  `surat_sehat` varchar(255) DEFAULT NULL,
  `kartu_tanda_mahasiswa` varchar(255) DEFAULT NULL,
  `ktp` varchar(255) DEFAULT NULL,
  `kartu_keluarga` varchar(255) DEFAULT NULL,
  `sim` varchar(255) DEFAULT NULL,
  `stnk` varchar(255) DEFAULT NULL,
  `skck` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `berkas_peserta`
--

INSERT INTO `berkas_peserta` (`id`, `id_peserta`, `surat_pengantar_magang`, `proposal_magang`, `curriculum_vitae`, `surat_pembuatan_idcard`, `surat_penerimaan`, `pas_foto`, `surat_sehat`, `kartu_tanda_mahasiswa`, `ktp`, `kartu_keluarga`, `sim`, `stnk`, `skck`) VALUES
(3, 3, 'static/uploads\\File_Testing_Upload_CV.pdf', 'static/uploads\\File_Testing_Upload_CV.pdf', 'static/uploads\\File_Testing_Upload_CV.pdf', 'uploads\\File_Testing_Surat_IDCARD.pdf', 'uploads\\File_Testing_Surat_Penerimaan_Magang.pdf', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 4, 'uploads\\File_Testing_Upload_Surat_Pengantar.pdf', 'uploads\\File_Testing_Upload_Proposal_Magang.pdf', 'uploads\\File_Testing_Upload_CV.pdf', 'uploads\\File_Testing_Surat_IDCARD.pdf', 'uploads\\File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads\\Contoh_File_Pas_Foto.pdf', 'uploads\\File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads\\File_Testing_KTM.pdf', 'uploads\\File_Testing_KTP.pdf', 'uploads\\File_Testing_Kartu_Keluarga.pdf', 'uploads\\File_Testing_SIM.pdf', 'uploads\\File_Testing_STNK.pdf', 'uploads\\File_Testing_SKCK.pdf'),
(21, 5, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(32, 6, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(33, 7, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(34, 8, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(35, 9, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(37, 11, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(38, 12, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(39, 13, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(40, 14, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(41, 15, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(42, 16, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(43, 17, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(44, 18, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(45, 19, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(46, 20, 'uploads/File_Testing_Upload_Surat_Pengantar.pdf', 'uploads/File_Testing_Upload_Proposal_Magang.pdf', 'uploads/File_Testing_Upload_CV.pdf', 'uploads/File_Testing_Surat_IDCARD.pdf', 'uploads/File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads/Contoh_File_Pas_Foto.pdf', 'uploads/File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads/File_Testing_KTM.pdf', 'uploads/File_Testing_KTP.pdf', 'uploads/File_Testing_Kartu_Keluarga.pdf', 'uploads/File_Testing_SIM.pdf', 'uploads/File_Testing_STNK.pdf', 'uploads/File_Testing_SKCK.pdf'),
(47, 21, 'uploads\\File_Testing_Upload_Surat_Pengantar.pdf', 'uploads\\File_Testing_Upload_Proposal_Magang.pdf', 'uploads\\File_Testing_Upload_CV.pdf', 'uploads\\File_Testing_Surat_Penerimaan_Magang.pdf', 'uploads\\File_Testing_Surat_IDCARD.pdf', 'uploads\\Contoh_File_Pas_Foto.pdf', 'uploads\\File_Testing_Surat_Keterangan_Sehat.pdf', 'uploads\\File_Testing_KTM.pdf', 'uploads\\File_Testing_KTP.pdf', 'uploads\\File_Testing_Kartu_Keluarga.pdf', 'uploads\\File_Testing_SIM.pdf', 'uploads\\File_Testing_STNK.pdf', 'uploads\\File_Testing_SKCK.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `data_berkas_hc`
--

CREATE TABLE `data_berkas_hc` (
  `id` int(11) NOT NULL,
  `template_surat_pembuatan_idcard` varchar(255) DEFAULT NULL,
  `template_surat_penerimaan_prakerin` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `data_peserta`
--

CREATE TABLE `data_peserta` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `nohp` varchar(20) NOT NULL,
  `semester` int(11) NOT NULL,
  `asal_kampus` varchar(100) NOT NULL,
  `jenis_kelamin` varchar(50) NOT NULL,
  `tempat_tanggal_lahir` varchar(100) NOT NULL,
  `tanggal_dimulai` date NOT NULL,
  `tanggal_berakhir` date NOT NULL,
  `nama_pembimbing` varchar(100) DEFAULT NULL,
  `nohp_pembimbing` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_peserta`
--

INSERT INTO `data_peserta` (`id`, `id_user`, `nama`, `nohp`, `semester`, `asal_kampus`, `jenis_kelamin`, `tempat_tanggal_lahir`, `tanggal_dimulai`, `tanggal_berakhir`, `nama_pembimbing`, `nohp_pembimbing`) VALUES
(3, 10, 'AAA', '123123', 4, 'Universitas Dummy', 'Perempuan', 'Bandung, 17 April 2002', '2025-01-07', '2025-01-24', NULL, NULL),
(4, 3, 'Peserta 1', '089878756', 7, 'Universitas Dummy', 'Laki-Laki', 'Bandung, 17 April 2002', '2025-01-06', '2025-01-22', 'Pebimbing Dummy ABD', '08888881'),
(5, 5, 'Peserta 5', '08123456705', 4, 'Universitas E', 'Perempuan', 'Bandung, 05/05/2001', '2025-01-18', '2025-03-18', 'Pembimbing 5', '08134567895'),
(6, 6, 'Peserta 6', '08123456706', 8, 'Universitas F', 'Laki-laki', 'Jakarta, 06/06/2000', '2025-01-20', '2025-03-20', 'Pembimbing 6', '08134567896'),
(7, 7, 'Peserta 7', '08123456707', 5, 'Universitas G', 'Perempuan', 'Malang, 07/07/2002', '2025-01-25', '2025-03-25', 'Pembimbing 7', '08134567897'),
(8, 8, 'Peserta 8', '08123456708', 7, 'Universitas H', 'Laki-laki', 'Semarang, 08/08/2001', '2025-01-27', '2025-03-27', 'Pembimbing 8', '08134567898'),
(9, 9, 'Peserta 9', '08123456709', 6, 'Universitas I', 'Perempuan', 'Jogja, 09/09/2002', '2025-01-30', '2025-03-30', 'Pembimbing 9', '08134567899'),
(11, 11, 'Peserta 11', '08123456711', 5, 'Universitas K', 'Laki-laki', 'Aceh, 11/11/2001', '2025-02-01', '2025-04-01', 'Pembimbing 11', '08134567911'),
(12, 12, 'Peserta 12', '08123456712', 4, 'Universitas L', 'Perempuan', 'Medan, 12/12/2000', '2025-02-05', '2025-04-05', 'Pembimbing 12', '08134567912'),
(13, 13, 'Peserta 13', '08123456713', 7, 'Universitas M', 'Laki-laki', 'Bali, 13/03/2001', '2025-02-10', '2025-04-10', 'Pembimbing 13', '08134567913'),
(14, 14, 'Peserta 14', '08123456714', 6, 'Universitas N', 'Perempuan', 'Makassar, 14/04/2002', '2025-02-12', '2025-04-12', 'Pembimbing 14', '08134567914'),
(15, 15, 'Peserta 15', '08123456715', 8, 'Universitas O', 'Laki-laki', 'Palembang, 15/05/2000', '2025-02-15', '2025-04-15', 'Pembimbing 15', '08134567915'),
(16, 16, 'Peserta 16', '08123456716', 4, 'Universitas P', 'Perempuan', 'Surabaya, 16/06/2001', '2025-02-20', '2025-04-20', 'Pembimbing 16', '08134567916'),
(17, 17, 'Peserta 17', '08123456717', 6, 'Universitas Q', 'Laki-laki', 'Jakarta, 17/07/2002', '2025-02-22', '2025-04-22', 'Pembimbing 17', '08134567917'),
(18, 18, 'Peserta 18', '08123456718', 5, 'Universitas R', 'Perempuan', 'Bandung, 18/08/2000', '2025-02-25', '2025-04-25', 'Pembimbing 18', '08134567918'),
(19, 19, 'Peserta 19', '08123456719', 4, 'Universitas S', 'Laki-laki', 'Jogja, 19/09/2001', '2025-03-01', '2025-05-01', 'Pembimbing 19', '08134567919'),
(20, 20, 'Peserta 20', '08123456720', 7, 'Universitas T', 'Perempuan', 'Medan, 20/10/2002', '2025-03-05', '2025-05-05', 'Pembimbing 20', '08134567920'),
(21, 21, 'Aulia Syifa', '082215155709', 7, 'Universitas Telkom', 'Perempuan', 'Bandung, 15 Juni 2003', '2025-01-09', '2025-01-31', 'Pak Dudung', '0987664533');

-- --------------------------------------------------------

--
-- Table structure for table `status_pendaftaran`
--

CREATE TABLE `status_pendaftaran` (
  `id` int(11) NOT NULL,
  `id_peserta` int(11) NOT NULL,
  `status_daftar` varchar(50) NOT NULL,
  `nama_divisi` varchar(50) DEFAULT NULL,
  `status_berkas` varchar(50) DEFAULT NULL,
  `catatan` text DEFAULT NULL,
  `tanggal_wawancara` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `status_pendaftaran`
--

INSERT INTO `status_pendaftaran` (`id`, `id_peserta`, `status_daftar`, `nama_divisi`, `status_berkas`, `catatan`, `tanggal_wawancara`) VALUES
(3, 3, 'Kel. Berkas', 'Kendaraan Khusus', 'Menunggu Peserta', NULL, '2025-01-07 00:13:15'),
(4, 4, 'Diterima', 'Divisi Dummy ABCD', 'Sesuai', NULL, '2025-01-08 02:00:00'),
(42, 5, 'Ditolak', 'Divisi B', 'Tidak Sesuai', 'Berkas kurang lengkap.', '2025-01-06 22:37:01'),
(43, 6, 'Diterima', 'Divisi C', 'Sedang Diproses', 'Menunggu hasil wawancara.', '2025-02-02 17:00:00'),
(44, 7, 'Kel. Berkas', 'Divisi D', 'Revisi', 'Harus melakukan revisi.', '2025-01-06 22:37:01'),
(45, 8, 'Perlu Diseleksi', 'Divisi E', 'Menunggu', 'Menunggu proses seleksi.', '2025-01-06 22:37:01'),
(46, 9, 'Diterima', 'Divisi F', 'Sesuai', 'Berkas telah diperiksa dan lengkap.', '2025-02-09 17:00:00'),
(47, 11, 'Ditolak', 'Divisi G', 'Tidak Sesuai', 'Berkas foto kurang jelas.', '2025-01-06 22:37:01'),
(48, 12, 'Kel. Berkas', 'Divisi H', 'Revisi', 'Revisi diperlukan pada surat sehat.', '2025-01-06 22:37:01'),
(49, 13, 'Wawancara', 'Divisi I', 'Sedang Diproses', 'Menunggu hasil wawancara.', '2025-02-07 17:00:00'),
(50, 14, 'Perlu Diseleksi', 'Divisi J', 'Menunggu', 'Menunggu persetujuan seleksi.', '2025-01-06 22:37:01'),
(51, 15, 'Diterima', 'Divisi K', 'Sesuai', 'Semua berkas sudah sesuai.', '2025-02-04 17:00:00'),
(52, 16, 'Ditolak', 'Divisi L', 'Tidak Sesuai', 'Proposal kurang lengkap.', '2025-01-06 22:37:01'),
(53, 17, 'Kel. Berkas', 'Divisi M', 'Revisi', 'Revisi pada CV diperlukan.', '2025-01-06 22:37:01'),
(54, 18, 'Wawancara', 'Divisi N', 'Sedang Diproses', 'Menunggu jadwal wawancara.', '2025-02-11 17:00:00'),
(55, 19, 'Diterima', 'Divisi O', 'Sesuai', 'Semua berkas telah memenuhi syarat.', '2025-02-19 17:00:00'),
(56, 20, 'Perlu Diseleksi', 'Divisi P', 'Menunggu', 'Dalam proses seleksi awal.', '2025-01-06 22:37:01'),
(57, 21, 'Wawancara', 'Alat Berat', 'Sesuai', NULL, '2025-01-21 02:04:58');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `roles` varchar(50) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `nohp` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `roles`, `nama`, `nohp`) VALUES
(1, 'adminhc@gmail.com', '12345', 'HC Admin', 'HC Admin', '0'),
(2, 'adminpam@gmail.com', '12345', 'PAM Admin', 'PAM Admin', '0'),
(3, 'peserta@gmail.com', '12345', 'Peserta', 'Peserta 1', '089878756'),
(4, 'user4@mail.com', '12345', 'Peserta', 'Peserta 4', '08123456704'),
(5, 'user5@mail.com', '12345', 'Peserta', 'Peserta 5', '08123456705'),
(6, 'user6@mail.com', '12345', 'Peserta', 'Peserta 6', '08123456706'),
(7, 'user7@mail.com', '12345', 'Peserta', 'Peserta 7', '08123456707'),
(8, 'user8@mail.com', '12345', 'Peserta', 'Peserta 8', '08123456708'),
(9, 'user9@mail.com', '12345', 'Peserta', 'Peserta 9', '08123456709'),
(10, 'AAA@mail.com', '12345', 'Peserta', 'AAA', '123123'),
(11, 'user11@mail.com', '12345', 'Peserta', 'Peserta 11', '08123456711'),
(12, 'user12@mail.com', '12345', 'Peserta', 'Peserta 12', '08123456712'),
(13, 'user13@mail.com', '12345', 'Peserta', 'Peserta 13', '08123456713'),
(14, 'user14@mail.com', '12345', 'Peserta', 'Peserta 14', '08123456714'),
(15, 'user15@mail.com', '12345', 'Peserta', 'Peserta 15', '08123456715'),
(16, 'user16@mail.com', '12345', 'Peserta', 'Peserta 16', '08123456716'),
(17, 'user17@mail.com', '12345', 'Peserta', 'Peserta 17', '08123456717'),
(18, 'user18@mail.com', '12345', 'Peserta', 'Peserta 18', '08123456718'),
(19, 'user19@mail.com', '12345', 'Peserta', 'Peserta 19', '08123456719'),
(20, 'user20@mail.com', '12345', 'Peserta', 'Peserta 20', '08123456720'),
(21, 'auliasyifa@gmail.com', '1234', 'Peserta', 'Aulia Syifa', '082215155709');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `berkas_peserta`
--
ALTER TABLE `berkas_peserta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_peserta` (`id_peserta`);

--
-- Indexes for table `data_berkas_hc`
--
ALTER TABLE `data_berkas_hc`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `data_peserta`
--
ALTER TABLE `data_peserta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_user` (`id_user`);

--
-- Indexes for table `status_pendaftaran`
--
ALTER TABLE `status_pendaftaran`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_peserta` (`id_peserta`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `berkas_peserta`
--
ALTER TABLE `berkas_peserta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `data_berkas_hc`
--
ALTER TABLE `data_berkas_hc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `data_peserta`
--
ALTER TABLE `data_peserta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `status_pendaftaran`
--
ALTER TABLE `status_pendaftaran`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `berkas_peserta`
--
ALTER TABLE `berkas_peserta`
  ADD CONSTRAINT `berkas_peserta_ibfk_1` FOREIGN KEY (`id_peserta`) REFERENCES `data_peserta` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `data_peserta`
--
ALTER TABLE `data_peserta`
  ADD CONSTRAINT `data_peserta_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `status_pendaftaran`
--
ALTER TABLE `status_pendaftaran`
  ADD CONSTRAINT `status_pendaftaran_ibfk_1` FOREIGN KEY (`id_peserta`) REFERENCES `data_peserta` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
