#!/usr/bin/env python2.7
import argparse
from pjp.classdir import ClassDir
from pjp.classfile import ClassFile
from pjp.jarfile import JarFile


def dump_class(class_):
    print 'this: %s' % class_.this_class
    print 'super: %s' % class_.super_class

    print 'Constants:'
    for constant in class_.constant_pool:
        print '  %s' % constant
    print

    print '  Interfaces:'
    for interface in class_.interfaces:
        print '    %s' % interface
    print

    print '  Methods:'
    for method in class_.methods.values():
        print '    %s' % method
        for attribute in method.attributes:
            print '      %s' % attribute
            if hasattr(attribute, 'attributes'):
                for inner_attrib in attribute.attributes:
                    print '        %s' % inner_attrib
            if attribute.type == 'Exceptions':
                for exception in attribute.exception_table:
                    print '        %s' % exception
    print

    print '  Fields:'
    for field in class_.fields.values():
        print '    %s' % field
        for attribute in field.attributes:
            print '      %s' % attribute
            if hasattr(attribute, 'attributes'):
                for inner_attrib in attribute.attributes:
                    print '        %s' % inner_attrib
    print

    print '  Attributes:'
    for attribute in class_.attributes:
        print '    %s' % attribute
    print


def main():
    parser = argparse.ArgumentParser(description='Dump class file')
    parser.add_argument('class_dir', help='class directory')
    args = parser.parse_args()

    class_dir = ClassDir(args.class_dir)
    for cls in class_dir.classes:
        class_ = ClassFile(class_dir[cls])

        print 'Class: %s' % cls
        dump_class(class_)

if __name__ == '__main__':
    main()
