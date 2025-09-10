# Coreform Cubit Mesh Export

Coreform Cubitから様々な形式のメッシュファイルをエクスポートするPythonライブラリ

## インストール方法

### PyPIから直接インストール（推奨）
```bash
pip install --upgrade coreform-cubit-mesh-export
```

### Cubit内蔵Pythonの場合
```bash
cd "C:\Program Files\Coreform Cubit 2025.3\bin\python3\"
python.exe -m pip install --upgrade coreform-cubit-mesh-export
```

### 開発版をGitHubからインストール
```bash
pip install git+https://github.com/ksugahar/Coreform_Cubit_Mesh_Export.git
```

### ローカルインストール（開発用）
```bash
git clone https://github.com/ksugahar/Coreform_Cubit_Mesh_Export.git
cd Coreform_Cubit_Mesh_Export
pip install -e .
```

## サポートしているファイル形式

- **Gmsh形式**
  - バージョン2.2（完全サポート）
  - バージョン4.1（部分サポート）
- **Nastran形式**
  - 2Dメッシュ
  - 3Dメッシュ
- **MEG形式**（ELF用）
  - 2Dメッシュ
  - 3Dメッシュ
- **VTK形式**
  - メッシュのみ（Legacy VTK形式）

## 使い方

### Cubit内での使用例

Cubitでメッシュ生成後、以下のようにPythonスクリプトを実行します：

```python
# Cubitコマンドライン
play "export_mesh.py"
```

`export_mesh.py`の内容例：

```python
import cubit_mesh_export

# Nastran形式でエクスポート
FileName = 'output/model.nas'
cubit_mesh_export.export_3D_Nastran(cubit, FileName)

# Gmsh形式でエクスポート
FileName = 'output/model.msh'
cubit_mesh_export.export_3D_gmsh_ver2(cubit, FileName)

# VTK形式でエクスポート
FileName = 'output/model.vtk'
cubit_mesh_export.export_3D_vtk(cubit, FileName)
```

## 関数一覧

### Gmsh形式
- `export_3D_gmsh_ver2(cubit, filename)` - Gmsh v2.2形式で3Dメッシュをエクスポート
- `export_3D_gmsh_ver4(cubit, filename)` - Gmsh v4.1形式で3Dメッシュをエクスポート（部分サポート）

### Nastran形式
- `export_2D_Nastran(cubit, filename)` - 2DメッシュをNastran形式でエクスポート
- `export_3D_Nastran(cubit, filename)` - 3DメッシュをNastran形式でエクスポート

### MEG形式（ELF用）
- `export_2D_meg(cubit, filename)` - 2DメッシュをMEG形式でエクスポート
- `export_3D_meg(cubit, filename)` - 3DメッシュをMEG形式でエクスポート

### VTK形式
- `export_3D_vtk(cubit, filename)` - 3DメッシュをVTK形式でエクスポート

## 要件

- Python 3.7以上
- NumPy >= 1.20.3
- SciPy >= 1.6.3
- Coreform Cubit（メッシュ生成用）

## ライセンス

BSD 3-Clause License

## 作者

Kengo Sugahara (ksugahar@gmail.com)

## リポジトリ

- GitHub: [https://github.com/ksugahar/Coreform_Cubit_Mesh_Export](https://github.com/ksugahar/Coreform_Cubit_Mesh_Export)
- PyPI: [https://pypi.org/project/coreform-cubit-mesh-export/](https://pypi.org/project/coreform-cubit-mesh-export/)

## バグ報告・機能要望

[GitHub Issues](https://github.com/ksugahar/Coreform_Cubit_Mesh_Export/issues)にてお願いします。

## 変更履歴

### v0.9.4 (2025-09-11)
- **バグ修正**
  - Gmsh v4形式: Wedge要素のノード出力を4個から6個に修正
  - Gmsh v4形式: 要素タグを0ではなく1から開始するよう修正
  - Gmsh v4形式: 空の要素リストでmin/max関数がエラーになる問題を修正
  - VTK形式: WedgeとPyramid要素のconnectivity取得処理が欠落していた問題を修正
  - NASTRAN形式: f-string構文エラーを修正
  - FreeFEM形式: 未定義変数`nodeset_surface_list`の問題を修正
  - geo_mesh形式: 未定義変数`nodes`の初期化を追加

### v0.9.3 (2025-01)
- パッケージ名を`Coreform_Cubit_Mesh_Export`に統一
- `pyproject.toml`ベースの最新パッケージング方式に移行
- ドキュメントの改善

### v0.9.2
- 初回PyPIリリース