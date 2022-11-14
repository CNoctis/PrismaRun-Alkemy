USE [master]
GO
/****** Object:  Database [Curso]    Script Date: 3/11/2022 16:51:10 ******/
CREATE DATABASE [Curso]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Curso', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS01\MSSQL\DATA\Curso.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Curso_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS01\MSSQL\DATA\Curso_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [Curso] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Curso].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Curso] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Curso] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Curso] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Curso] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Curso] SET ARITHABORT OFF 
GO
ALTER DATABASE [Curso] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [Curso] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Curso] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Curso] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Curso] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Curso] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Curso] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Curso] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Curso] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Curso] SET  ENABLE_BROKER 
GO
ALTER DATABASE [Curso] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Curso] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Curso] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Curso] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Curso] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Curso] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Curso] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Curso] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [Curso] SET  MULTI_USER 
GO
ALTER DATABASE [Curso] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Curso] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Curso] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Curso] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Curso] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Curso] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [Curso] SET QUERY_STORE = OFF
GO
USE [Curso]
GO
/****** Object:  Table [dbo].[Alumno]    Script Date: 3/11/2022 16:51:11 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Alumno](
	[Legajo] [int] NOT NULL,
	[Nombre] [varchar](30) NOT NULL,
	[Apellido] [varchar](30) NOT NULL,
	[Fecha_Nacimiento] [date] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Legajo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cursa]    Script Date: 3/11/2022 16:51:11 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cursa](
	[LegajoAlumno] [int] NULL,
	[CodigoMateria] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Materia]    Script Date: 3/11/2022 16:51:11 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Materia](
	[Codigo] [int] NOT NULL,
	[descripcion] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD FOREIGN KEY([CodigoMateria])
REFERENCES [dbo].[Materia] ([Codigo])
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD FOREIGN KEY([LegajoAlumno])
REFERENCES [dbo].[Alumno] ([Legajo])
GO
USE [master]
GO
ALTER DATABASE [Curso] SET  READ_WRITE 
GO