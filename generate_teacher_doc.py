#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Teacher Document Generator for ChatGPT K-12 / SheerID Verification
Powered by Yowes Engine
"""

import os
import sys
from pathlib import Path

# Add yowes to sys.path
YOWES_DIR = Path("d:/FREELANCE/yowes")
if not YOWES_DIR.exists():
    YOWES_DIR = Path(__file__).resolve().parent.parent / "yowes"

if str(YOWES_DIR) not in sys.path:
    sys.path.insert(0, str(YOWES_DIR))

try:
    from countries.us import USGenerator
except ImportError as e:
    print(f"Error loading yowes generator: {e}")
    sys.exit(1)

def generate_documents(first_name=None, last_name=None, school_name=None, output_dir=None):
    if output_dir is None:
        output_dir = Path(__file__).resolve().parent / "generated_docs"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    gen = USGenerator()
    
    # Name
    if not first_name or not last_name:
        f, l = gen.generate_name()
        first_name = first_name or f
        last_name = last_name or l
        
    full_name = f"{first_name} {last_name}"
    
    # School
    if school_name:
        school = gen.search_school(school_name) or gen.random_school()
    else:
        school = gen.random_school()
        
    position = gen.random_position()
    dob = "1987-06-15"
    
    print("=" * 60)
    print("  TEACHER DOCUMENT GENERATOR (US K-12)")
    print("=" * 60)
    print(f"  [+] Teacher Name : {full_name}")
    print(f"  [+] School Name  : {school.get('name')}")
    print(f"  [+] District/LEA : {school.get('lea', 'N/A')}")
    print(f"  [+] Location     : {school.get('town')}, {school.get('state')}")
    print(f"  [+] Position     : {position}")
    print("-" * 60)
    
    results = {}
    doc_types = ["employment_letter", "teacher_id", "teaching_license"]
    
    for doc_type in doc_types:
        try:
            doc_bytes = gen.generate_document(doc_type, first_name, last_name, school, position, dob)
            filename = f"{first_name}_{last_name}_{doc_type}.png"
            file_path = output_dir / filename
            with open(file_path, "wb") as f:
                f.write(doc_bytes)
            print(f"  [OK] Generated: {filename} ({len(doc_bytes):,} bytes)")
            results[doc_type] = str(file_path)
        except Exception as e:
            print(f"  [!] Failed to generate {doc_type}: {e}")
            
    print("=" * 60)
    print(f"Dokumen berhasil disimpan di: {output_dir}")
    return results

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate US Teacher Verification Documents")
    parser.add_argument("--first", help="First name")
    parser.add_argument("--last", help="Last name")
    parser.add_argument("--school", help="School name query")
    parser.add_argument("--out", help="Output directory")
    args = parser.parse_args()
    
    generate_documents(args.first, args.last, args.school, args.out)
