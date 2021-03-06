#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Sat Apr 16 23:17:08 2022 by generateDS.py version 2.40.10.
# Python 3.9.7 | packaged by conda-forge | (default, Sep 29 2021, 19:24:02)  [Clang 11.1.0 ]
#
# Command line options:
#   ('-o', 'CFDI40.py')
#   ('-s', 'CFDI40_sub.py')
#
# Command line arguments:
#   cfdv40.xsd.xml
#
# Command line:
#   /opt/homebrew/Caskroom/miniforge/base/bin/generateDS -o "CFDI40.py" -s "CFDI40_sub.py" cfdv40.xsd.xml
#
# Current working directory (os.getcwd()):
#   suppourt-files
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = ""
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {
        # 'Comprobante': 'xsi:schemaLocation="http://www.sat.gob.mx/cfd/4 http://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd"',
    }
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {
        # 'Comprobante': 'schemaLocation',
    }

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': self.__class__.__name__,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            if sys.version_info.major == 2:
                from StringIO import StringIO
            else:
                from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % float(input_data)).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.strftime('%Y-%m-%dT%H:%M:%S')
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            target = str(target)
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class c_ClaveProdServ(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_ClaveUnidad(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_CodigoPostal(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Colonia(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Estado(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Exportacion(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_FormaPago(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Impuesto(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Localidad(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Meses(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_MetodoPago(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Moneda(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Municipio(str):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validar()

    def validar(self):
        if not self.isdigit():
            raise ValueError('El valor debe ser un n??mero entero')
        if len(self) != 5:
            raise ValueError('El valor debe tener 5 d??gitos')
    
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_ObjetoImp(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Pais(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_Periodicidad(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_RegimenFiscal(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_TipoDeComprobante(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_TipoFactor(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_TipoRelacion(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class c_UsoCFDI(str):
    def __eq__(self, other):
        if type(other) is type(self):
            return str.__eq__(self, other)
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return str.__hash__(self)

class Comprobante(GeneratedsSuper):
    """Comprobante -- Est
    ??
    ndar de Comprobante Fiscal Digital por Internet.
    Version -- Atributo requerido con valor prefijado a 4.0 que indica la versi
    ??
    n del est
    ??
    ndar bajo el que se encuentra expresado el comprobante.
    Serie -- Atributo opcional para precisar la serie para control interno del contribuyente. Este atributo acepta una cadena de caracteres.
    Folio -- Atributo opcional para control interno del contribuyente que expresa el folio del comprobante, acepta una cadena de caracteres.
    Fecha -- Atributo requerido para la expresi
    ??
    n de la fecha y hora de expedici
    ??
    n del Comprobante Fiscal Digital por Internet. Se expresa en la forma AAAA-MM-DDThh:mm:ss y debe corresponder con la hora local donde se expide el comprobante.
    Sello -- Atributo requerido para contener el sello digital del comprobante fiscal, al que hacen referencia las reglas de resoluci
    ??
    n miscel
    ??
    nea vigente. El sello debe ser expresado como una cadena de texto en formato Base 64.
    FormaPago -- Atributo condicional para expresar la clave de la forma de pago de los bienes o servicios amparados por el comprobante.
    NoCertificado -- Atributo requerido para expresar el n
    ??
    mero de serie del certificado de sello digital que ampara al comprobante, de acuerdo con el acuse correspondiente a 20 posiciones otorgado por el sistema del SAT.
    Certificado -- Atributo requerido que sirve para incorporar el certificado de sello digital que ampara al comprobante, como texto en formato base 64.
    CondicionesDePago -- Atributo condicional para expresar las condiciones comerciales aplicables para el pago del comprobante fiscal digital por Internet. Este atributo puede ser condicionado mediante atributos o complementos.
    SubTotal -- Atributo requerido para representar la suma de los importes de los conceptos antes de descuentos e impuesto. No se permiten valores negativos.
    Descuento -- Atributo condicional para representar el importe total de los descuentos aplicables antes de impuestos. No se permiten valores negativos. Se debe registrar cuando existan conceptos con descuento.
    Moneda -- Atributo requerido para identificar la clave de la moneda utilizada para expresar los montos, cuando se usa moneda nacional se registra MXN. Conforme con la especificaci
    ??
    n ISO 4217.
    TipoCambio -- Atributo condicional para representar el tipo de cambio FIX conforme con la moneda usada. Es requerido cuando la clave de moneda es distinta de MXN y de XXX. El valor debe reflejar el n
    ??
    mero de pesos mexicanos que equivalen a una unidad de la divisa se
    ??
    alada en el atributo moneda. Si el valor est
    ??
    fuera del porcentaje aplicable a la moneda tomado del cat
    ??
    logo c_Moneda, el emisor debe obtener del PAC que vaya a timbrar el CFDI, de manera no autom
    ??
    tica, una clave de confirmaci
    ??
    n para ratificar que el valor es correcto e integrar dicha clave en el atributo Confirmacion.
    Total -- Atributo requerido para representar la suma del subtotal, menos los descuentos aplicables, m
    ??
    s las contribuciones recibidas (impuestos trasladados - federales y/o locales, derechos, productos, aprovechamientos, aportaciones de seguridad social, contribuciones de mejoras) menos los impuestos retenidos federales y/o locales. Si el valor es superior al l
    ??
    mite que establezca el SAT en la Resoluci
    ??
    n Miscel
    ??
    nea Fiscal vigente, el emisor debe obtener del PAC que vaya a timbrar el CFDI, de manera no autom
    ??
    tica, una clave de confirmaci
    ??
    n para ratificar que el valor es correcto e integrar dicha clave en el atributo Confirmacion. No se permiten valores negativos.
    TipoDeComprobante -- Atributo requerido para expresar la clave del efecto del comprobante fiscal para el contribuyente emisor.
    Exportacion -- Atributo requerido para expresar si el comprobante ampara una operaci
    ??
    n de exportaci
    ??
    n.
    MetodoPago -- Atributo condicional para precisar la clave del m
    ??
    todo de pago que aplica para este comprobante fiscal digital por Internet, conforme al Art
    ??
    culo 29-A fracci
    ??
    n VII incisos a y b del CFF.
    LugarExpedicion -- Atributo requerido para incorporar el c
    ??
    digo postal del lugar de expedici
    ??
    n del comprobante (domicilio de la matriz o de la sucursal).
    Confirmacion -- Atributo condicional para registrar la clave de confirmaci
    ??
    n que entregue el PAC para expedir el comprobante con importes grandes, con un tipo de cambio fuera del rango establecido o con ambos casos. Es requerido cuando se registra un tipo de cambio o un total fuera del rango establecido.
    InformacionGlobal -- Nodo condicional para precisar la informaci
    ??
    n relacionada con el comprobante global.
    CfdiRelacionados -- Nodo opcional para precisar la informaci
    ??
    n de los comprobantes relacionados.
    Emisor -- Nodo requerido para expresar la informaci
    ??
    n del contribuyente emisor del comprobante.
    Receptor -- Nodo requerido para precisar la informaci
    ??
    n del contribuyente receptor del comprobante.
    Conceptos -- Nodo requerido para listar los conceptos cubiertos por el comprobante.
    Impuestos -- Nodo condicional para expresar el resumen de los impuestos aplicables.
    Complemento -- Nodo opcional donde se incluye el complemento Timbre Fiscal Digital de manera obligatoria y los nodos complementarios determinados por el SAT, de acuerdo con las disposiciones particulares para un sector o actividad espec
    ??
    fica.
    Addenda -- Nodo opcional para recibir las extensiones al presente formato que sean de utilidad al contribuyente. Para las reglas de uso del mismo, referirse al formato origen.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Version='4.0', Serie=None, Folio=None, Fecha=None, Sello=None, FormaPago=None, NoCertificado=None, Certificado=None, CondicionesDePago=None, SubTotal=None, Descuento=None, Moneda=None, TipoCambio=None, Total=None, TipoDeComprobante=None, Exportacion=None, MetodoPago=None, LugarExpedicion=None, Confirmacion=None, InformacionGlobal=None, CfdiRelacionados=None, Emisor=None, Receptor=None, Conceptos=None, Impuestos=None, Complemento=None, Addenda=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "cfdi"
        self.Version = _cast(None, Version)
        self.Version_nsprefix_ = None
        self.Serie = _cast(None, Serie)
        self.Serie_nsprefix_ = None
        self.Folio = _cast(None, Folio)
        self.Folio_nsprefix_ = None
        self.Fecha = _cast(None, Fecha)
        self.Fecha_nsprefix_ = None
        self.Sello = _cast(None, Sello)
        self.Sello_nsprefix_ = None
        self.FormaPago = _cast(None, FormaPago)
        self.FormaPago_nsprefix_ = None
        self.NoCertificado = _cast(None, NoCertificado)
        self.NoCertificado_nsprefix_ = None
        self.Certificado = _cast(None, Certificado)
        self.Certificado_nsprefix_ = None
        self.CondicionesDePago = _cast(None, CondicionesDePago)
        self.CondicionesDePago_nsprefix_ = None
        self.SubTotal = _cast(None, SubTotal)
        self.SubTotal_nsprefix_ = None
        self.Descuento = _cast(None, Descuento)
        self.Descuento_nsprefix_ = None
        self.Moneda = _cast(None, Moneda)
        self.Moneda_nsprefix_ = None
        self.TipoCambio = _cast(float, TipoCambio)
        self.TipoCambio_nsprefix_ = None
        self.Total = _cast(None, Total)
        self.Total_nsprefix_ = None
        self.TipoDeComprobante = _cast(None, TipoDeComprobante)
        self.TipoDeComprobante_nsprefix_ = None
        self.Exportacion = _cast(None, Exportacion)
        self.Exportacion_nsprefix_ = None
        self.MetodoPago = _cast(None, MetodoPago)
        self.MetodoPago_nsprefix_ = None
        self.LugarExpedicion = _cast(None, LugarExpedicion)
        self.LugarExpedicion_nsprefix_ = None
        self.Confirmacion = _cast(None, Confirmacion)
        self.Confirmacion_nsprefix_ = None
        self.InformacionGlobal = InformacionGlobal
        self.InformacionGlobal_nsprefix_ = "cfdi"
        if CfdiRelacionados is None:
            self.CfdiRelacionados = []
        else:
            self.CfdiRelacionados = CfdiRelacionados
        self.CfdiRelacionados_nsprefix_ = "cfdi"
        self.Emisor = Emisor
        self.Emisor_nsprefix_ = "cfdi"
        self.Receptor = Receptor
        self.Receptor_nsprefix_ = "cfdi"
        self.Conceptos = Conceptos
        self.Conceptos_nsprefix_ = "cfdi"
        self.Impuestos = Impuestos
        self.Impuestos_nsprefix_ = "cfdi"
        self.Complemento = Complemento
        self.Complemento_nsprefix_ = "cfdi"
        self.Addenda = Addenda
        self.Addenda_nsprefix_ = "cfdi"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Comprobante)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Comprobante.subclass:
            return Comprobante.subclass(*args_, **kwargs_)
        else:
            return Comprobante(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_InformacionGlobal(self):
        return self.InformacionGlobal
    def set_InformacionGlobal(self, InformacionGlobal):
        self.InformacionGlobal = InformacionGlobal
    def get_CfdiRelacionados(self):
        return self.CfdiRelacionados
    def set_CfdiRelacionados(self, CfdiRelacionados):
        self.CfdiRelacionados = CfdiRelacionados
    def add_CfdiRelacionados(self, value):
        self.CfdiRelacionados.append(value)
    def insert_CfdiRelacionados_at(self, index, value):
        self.CfdiRelacionados.insert(index, value)
    def replace_CfdiRelacionados_at(self, index, value):
        self.CfdiRelacionados[index] = value
    def get_Emisor(self):
        return self.Emisor
    def set_Emisor(self, Emisor):
        self.Emisor = Emisor
    def get_Receptor(self):
        return self.Receptor
    def set_Receptor(self, Receptor):
        self.Receptor = Receptor
    def get_Conceptos(self):
        return self.Conceptos
    def set_Conceptos(self, Conceptos):
        self.Conceptos = Conceptos
    def get_Impuestos(self):
        return self.Impuestos
    def set_Impuestos(self, Impuestos):
        self.Impuestos = Impuestos
    def get_Complemento(self):
        return self.Complemento
    def set_Complemento(self, Complemento):
        self.Complemento = Complemento
    def get_Addenda(self):
        return self.Addenda
    def set_Addenda(self, Addenda):
        self.Addenda = Addenda
    def get_Version(self):
        return self.Version
    def set_Version(self, Version):
        self.Version = Version
    def get_Serie(self):
        return self.Serie
    def set_Serie(self, Serie):
        self.Serie = Serie
    def get_Folio(self):
        return self.Folio
    def set_Folio(self, Folio):
        self.Folio = Folio
    def get_Fecha(self):
        return self.Fecha
    def set_Fecha(self, Fecha):
        self.Fecha = Fecha
    def get_Sello(self):
        return self.Sello
    def set_Sello(self, Sello):
        self.Sello = Sello
    def get_FormaPago(self):
        return self.FormaPago
    def set_FormaPago(self, FormaPago):
        self.FormaPago = FormaPago
    def get_NoCertificado(self):
        return self.NoCertificado
    def set_NoCertificado(self, NoCertificado):
        self.NoCertificado = NoCertificado
    def get_Certificado(self):
        return self.Certificado
    def set_Certificado(self, Certificado):
        self.Certificado = Certificado
    def get_CondicionesDePago(self):
        return self.CondicionesDePago
    def set_CondicionesDePago(self, CondicionesDePago):
        self.CondicionesDePago = CondicionesDePago
    def get_SubTotal(self):
        return self.SubTotal
    def set_SubTotal(self, SubTotal):
        self.SubTotal = SubTotal
    def get_Descuento(self):
        return self.Descuento
    def set_Descuento(self, Descuento):
        self.Descuento = Descuento
    def get_Moneda(self):
        return self.Moneda
    def set_Moneda(self, Moneda):
        self.Moneda = Moneda
    def get_TipoCambio(self):
        return self.TipoCambio
    def set_TipoCambio(self, TipoCambio):
        self.TipoCambio = TipoCambio
    def get_Total(self):
        return self.Total
    def set_Total(self, Total):
        self.Total = Total
    def get_TipoDeComprobante(self):
        return self.TipoDeComprobante
    def set_TipoDeComprobante(self, TipoDeComprobante):
        self.TipoDeComprobante = TipoDeComprobante
    def get_Exportacion(self):
        return self.Exportacion
    def set_Exportacion(self, Exportacion):
        self.Exportacion = Exportacion
    def get_MetodoPago(self):
        return self.MetodoPago
    def set_MetodoPago(self, MetodoPago):
        self.MetodoPago = MetodoPago
    def get_LugarExpedicion(self):
        return self.LugarExpedicion
    def set_LugarExpedicion(self, LugarExpedicion):
        self.LugarExpedicion = LugarExpedicion
    def get_Confirmacion(self):
        return self.Confirmacion
    def set_Confirmacion(self, Confirmacion):
        self.Confirmacion = Confirmacion
    def validate_VersionType(self, value):
        # Validate type VersionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_SerieType(self, value):
        # Validate type SerieType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SerieType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on SerieType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_SerieType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_SerieType_patterns_, ))
    validate_SerieType_patterns_ = [['^([^|]{1,25})$']]
    def validate_FolioType(self, value):
        # Validate type FolioType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FolioType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FolioType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_FolioType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_FolioType_patterns_, ))
    validate_FolioType_patterns_ = [['^([^|]{1,40})$']]
    def validate_t_FechaH(self, value):
        # Validate type tdCFDI:t_FechaH, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (datetime_.datetime)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            if not self.gds_validate_simple_patterns(
                    self.validate_t_FechaH_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_FechaH_patterns_, ))
    validate_t_FechaH_patterns_ = [['^((20[1-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]))$']]
    def validate_SelloType(self, value):
        # Validate type SelloType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_c_FormaPago(self, value):
        # Validate type catCFDI:c_FormaPago, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = ['01', '02', '03', '04', '05', '06', '08', '12', '13', '14', '15', '17', '23', '24', '25', '26', '27', '28', '29', '30', '31', '99']
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_FormaPago' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False
    def validate_NoCertificadoType(self, value):
        # Validate type NoCertificadoType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on NoCertificadoType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NoCertificadoType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NoCertificadoType_patterns_, ))
    validate_NoCertificadoType_patterns_ = [['^([0-9]{20})$']]
    def validate_CertificadoType(self, value):
        # Validate type CertificadoType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_CondicionesDePagoType(self, value):
        # Validate type CondicionesDePagoType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CondicionesDePagoType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CondicionesDePagoType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CondicionesDePagoType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CondicionesDePagoType_patterns_, ))
    validate_CondicionesDePagoType_patterns_ = [['^([^|]{1,1000})$']]
    def validate_t_Importe(self, value):
        # Validate type tdCFDI:t_Importe, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on t_Importe' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_Importe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_Importe_patterns_, ))
    validate_t_Importe_patterns_ = [['^([0-9]{1,18}(.[0-9]{1,6})?)$']]
    def validate_c_Moneda(self, value):
        # Validate type catCFDI:c_Moneda, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = 
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_Moneda' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False
    def validate_TipoCambioType(self, value):
        # Validate type TipoCambioType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000001:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TipoCambioType' % {"value": value, "lineno": lineno} )
                result = False
    def validate_c_TipoDeComprobante(self, value):
        # Validate type catCFDI:c_TipoDeComprobante, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['I', 'E', 'T', 'N', 'P']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_TipoDeComprobante' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_c_Exportacion(self, value):
        # Validate type catCFDI:c_Exportacion, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['01', '02', '03', '04']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_Exportacion' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_c_MetodoPago(self, value):
        # Validate type catCFDI:c_MetodoPago, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = ['PUE', 'PPD']
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_MetodoPago' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False
    def validate_c_CodigoPostal(self, value):
        # Validate type catCFDI:c_CodigoPostal, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = 
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_CodigoPostal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False
    def validate_ConfirmacionType(self, value):
        # Validate type ConfirmacionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on ConfirmacionType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ConfirmacionType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ConfirmacionType_patterns_, ))
    validate_ConfirmacionType_patterns_ = [['^([0-9a-zA-Z]{5})$']]
    def _hasContent(self):
        if (
            self.InformacionGlobal is not None or
            self.CfdiRelacionados or
            self.Emisor is not None or
            self.Receptor is not None or
            self.Conceptos is not None or
            self.Impuestos is not None or
            self.Complemento is not None or
            self.Addenda is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='Comprobante', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Comprobante')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Comprobante':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Comprobante')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Comprobante', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Comprobante'):
        if self.Version is not None and 'Version' not in already_processed:
            already_processed.add('Version')
            outfile.write(' Version=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Version), input_name='Version')), ))
        if self.Serie is not None and 'Serie' not in already_processed:
            already_processed.add('Serie')
            outfile.write(' Serie=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Serie), input_name='Serie')), ))
        if self.Folio is not None and 'Folio' not in already_processed:
            already_processed.add('Folio')
            outfile.write(' Folio=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Folio), input_name='Folio')), ))
        if self.Fecha is not None and 'Fecha' not in already_processed:
            already_processed.add('Fecha')
            outfile.write(' Fecha="%s"' % self.Fecha)
        if self.Sello is not None and 'Sello' not in already_processed:
            already_processed.add('Sello')
            outfile.write(' Sello=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Sello), input_name='Sello')), ))
        if self.FormaPago is not None and 'FormaPago' not in already_processed:
            already_processed.add('FormaPago')
            outfile.write(' FormaPago=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.FormaPago), input_name='FormaPago')), ))
        if self.NoCertificado is not None and 'NoCertificado' not in already_processed:
            already_processed.add('NoCertificado')
            outfile.write(' NoCertificado=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.NoCertificado), input_name='NoCertificado')), ))
        if self.Certificado is not None and 'Certificado' not in already_processed:
            already_processed.add('Certificado')
            outfile.write(' Certificado=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Certificado), input_name='Certificado')), ))
        if self.CondicionesDePago is not None and 'CondicionesDePago' not in already_processed:
            already_processed.add('CondicionesDePago')
            outfile.write(' CondicionesDePago=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.CondicionesDePago), input_name='CondicionesDePago')), ))
        if self.SubTotal is not None and 'SubTotal' not in already_processed:
            already_processed.add('SubTotal')
            outfile.write(' SubTotal="%s"' % self.gds_format_decimal(self.SubTotal, input_name='SubTotal'))
        if self.Descuento is not None and 'Descuento' not in already_processed:
            already_processed.add('Descuento')
            outfile.write(' Descuento="%s"' % self.gds_format_decimal(self.Descuento, input_name='Descuento'))
        if self.Moneda is not None and 'Moneda' not in already_processed:
            already_processed.add('Moneda')
            outfile.write(' Moneda=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Moneda), input_name='Moneda')), ))
        if self.TipoCambio is not None and 'TipoCambio' not in already_processed:
            already_processed.add('TipoCambio')
            outfile.write(' TipoCambio="%s"' % self.gds_format_decimal(self.TipoCambio, input_name='TipoCambio'))
        if self.Total is not None and 'Total' not in already_processed:
            already_processed.add('Total')
            outfile.write(' Total="%s"' % self.gds_format_decimal(self.Total, input_name='Total'))
        if self.TipoDeComprobante is not None and 'TipoDeComprobante' not in already_processed:
            already_processed.add('TipoDeComprobante')
            outfile.write(' TipoDeComprobante=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.TipoDeComprobante), input_name='TipoDeComprobante')), ))
        if self.Exportacion is not None and 'Exportacion' not in already_processed:
            already_processed.add('Exportacion')
            outfile.write(' Exportacion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Exportacion), input_name='Exportacion')), ))
        if self.MetodoPago is not None and 'MetodoPago' not in already_processed:
            already_processed.add('MetodoPago')
            outfile.write(' MetodoPago=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.MetodoPago), input_name='MetodoPago')), ))
        if self.LugarExpedicion is not None and 'LugarExpedicion' not in already_processed:
            already_processed.add('LugarExpedicion')
            outfile.write(' LugarExpedicion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.LugarExpedicion), input_name='LugarExpedicion')), ))
        if self.Confirmacion is not None and 'Confirmacion' not in already_processed:
            already_processed.add('Confirmacion')
            outfile.write(' Confirmacion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Confirmacion), input_name='Confirmacion')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='Comprobante', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.InformacionGlobal is not None:
            namespaceprefix_ = self.InformacionGlobal_nsprefix_ + ':' if (UseCapturedNS_ and self.InformacionGlobal_nsprefix_) else ''
            self.InformacionGlobal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InformacionGlobal', pretty_print=pretty_print)
        for CfdiRelacionados_ in self.CfdiRelacionados:
            namespaceprefix_ = self.CfdiRelacionados_nsprefix_ + ':' if (UseCapturedNS_ and self.CfdiRelacionados_nsprefix_) else ''
            CfdiRelacionados_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CfdiRelacionados', pretty_print=pretty_print)
        if self.Emisor is not None:
            namespaceprefix_ = self.Emisor_nsprefix_ + ':' if (UseCapturedNS_ and self.Emisor_nsprefix_) else ''
            self.Emisor.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Emisor', pretty_print=pretty_print)
        if self.Receptor is not None:
            namespaceprefix_ = self.Receptor_nsprefix_ + ':' if (UseCapturedNS_ and self.Receptor_nsprefix_) else ''
            self.Receptor.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Receptor', pretty_print=pretty_print)
        if self.Conceptos is not None:
            namespaceprefix_ = self.Conceptos_nsprefix_ + ':' if (UseCapturedNS_ and self.Conceptos_nsprefix_) else ''
            self.Conceptos.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Conceptos', pretty_print=pretty_print)
        if self.Impuestos is not None:
            namespaceprefix_ = self.Impuestos_nsprefix_ + ':' if (UseCapturedNS_ and self.Impuestos_nsprefix_) else ''
            self.Impuestos.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Impuestos', pretty_print=pretty_print)
        if self.Complemento is not None:
            namespaceprefix_ = self.Complemento_nsprefix_ + ':' if (UseCapturedNS_ and self.Complemento_nsprefix_) else ''
            self.Complemento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Complemento', pretty_print=pretty_print)
        if self.Addenda is not None:
            namespaceprefix_ = self.Addenda_nsprefix_ + ':' if (UseCapturedNS_ and self.Addenda_nsprefix_) else ''
            self.Addenda.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Addenda', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Version', node)
        if value is not None and 'Version' not in already_processed:
            already_processed.add('Version')
            self.Version = value
            self.validate_VersionType(self.Version)    # validate type VersionType
        value = find_attr_value_('Serie', node)
        if value is not None and 'Serie' not in already_processed:
            already_processed.add('Serie')
            self.Serie = value
            self.validate_SerieType(self.Serie)    # validate type SerieType
        value = find_attr_value_('Folio', node)
        if value is not None and 'Folio' not in already_processed:
            already_processed.add('Folio')
            self.Folio = value
            self.validate_FolioType(self.Folio)    # validate type FolioType
        value = find_attr_value_('Fecha', node)
        if value is not None and 'Fecha' not in already_processed:
            already_processed.add('Fecha')
            try:
                self.Fecha = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (Fecha): %s' % exp)
            self.validate_t_FechaH(self.Fecha)    # validate type t_FechaH
        value = find_attr_value_('Sello', node)
        if value is not None and 'Sello' not in already_processed:
            already_processed.add('Sello')
            self.Sello = value
            self.validate_SelloType(self.Sello)    # validate type SelloType
        value = find_attr_value_('FormaPago', node)
        if value is not None and 'FormaPago' not in already_processed:
            already_processed.add('FormaPago')
            self.FormaPago = value
            self.validate_c_FormaPago(self.FormaPago)    # validate type c_FormaPago
        value = find_attr_value_('NoCertificado', node)
        if value is not None and 'NoCertificado' not in already_processed:
            already_processed.add('NoCertificado')
            self.NoCertificado = value
            self.validate_NoCertificadoType(self.NoCertificado)    # validate type NoCertificadoType
        value = find_attr_value_('Certificado', node)
        if value is not None and 'Certificado' not in already_processed:
            already_processed.add('Certificado')
            self.Certificado = value
            self.validate_CertificadoType(self.Certificado)    # validate type CertificadoType
        value = find_attr_value_('CondicionesDePago', node)
        if value is not None and 'CondicionesDePago' not in already_processed:
            already_processed.add('CondicionesDePago')
            self.CondicionesDePago = value
            self.validate_CondicionesDePagoType(self.CondicionesDePago)    # validate type CondicionesDePagoType
        value = find_attr_value_('SubTotal', node)
        if value is not None and 'SubTotal' not in already_processed:
            already_processed.add('SubTotal')
            value = self.gds_parse_decimal(value, node, 'SubTotal')
            self.SubTotal = value
            self.validate_t_Importe(self.SubTotal)    # validate type t_Importe
        value = find_attr_value_('Descuento', node)
        if value is not None and 'Descuento' not in already_processed:
            already_processed.add('Descuento')
            value = self.gds_parse_decimal(value, node, 'Descuento')
            self.Descuento = value
            self.validate_t_Importe(self.Descuento)    # validate type t_Importe
        value = find_attr_value_('Moneda', node)
        if value is not None and 'Moneda' not in already_processed:
            already_processed.add('Moneda')
            self.Moneda = value
            self.validate_c_Moneda(self.Moneda)    # validate type c_Moneda
        value = find_attr_value_('TipoCambio', node)
        if value is not None and 'TipoCambio' not in already_processed:
            already_processed.add('TipoCambio')
            value = self.gds_parse_decimal(value, node, 'TipoCambio')
            self.TipoCambio = value
            self.validate_TipoCambioType(self.TipoCambio)    # validate type TipoCambioType
        value = find_attr_value_('Total', node)
        if value is not None and 'Total' not in already_processed:
            already_processed.add('Total')
            value = self.gds_parse_decimal(value, node, 'Total')
            self.Total = value
            self.validate_t_Importe(self.Total)    # validate type t_Importe
        value = find_attr_value_('TipoDeComprobante', node)
        if value is not None and 'TipoDeComprobante' not in already_processed:
            already_processed.add('TipoDeComprobante')
            self.TipoDeComprobante = value
            self.validate_c_TipoDeComprobante(self.TipoDeComprobante)    # validate type c_TipoDeComprobante
        value = find_attr_value_('Exportacion', node)
        if value is not None and 'Exportacion' not in already_processed:
            already_processed.add('Exportacion')
            self.Exportacion = value
            self.validate_c_Exportacion(self.Exportacion)    # validate type c_Exportacion
        value = find_attr_value_('MetodoPago', node)
        if value is not None and 'MetodoPago' not in already_processed:
            already_processed.add('MetodoPago')
            self.MetodoPago = value
            self.validate_c_MetodoPago(self.MetodoPago)    # validate type c_MetodoPago
        value = find_attr_value_('LugarExpedicion', node)
        if value is not None and 'LugarExpedicion' not in already_processed:
            already_processed.add('LugarExpedicion')
            self.LugarExpedicion = value
            self.validate_c_CodigoPostal(self.LugarExpedicion)    # validate type c_CodigoPostal
        value = find_attr_value_('Confirmacion', node)
        if value is not None and 'Confirmacion' not in already_processed:
            already_processed.add('Confirmacion')
            self.Confirmacion = value
            self.validate_ConfirmacionType(self.Confirmacion)    # validate type ConfirmacionType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InformacionGlobal':
            obj_ = InformacionGlobalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InformacionGlobal = obj_
            obj_.original_tagname_ = 'InformacionGlobal'
        elif nodeName_ == 'CfdiRelacionados':
            obj_ = CfdiRelacionadosType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CfdiRelacionados.append(obj_)
            obj_.original_tagname_ = 'CfdiRelacionados'
        elif nodeName_ == 'Emisor':
            obj_ = EmisorType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Emisor = obj_
            obj_.original_tagname_ = 'Emisor'
        elif nodeName_ == 'Receptor':
            obj_ = ReceptorType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Receptor = obj_
            obj_.original_tagname_ = 'Receptor'
        elif nodeName_ == 'Conceptos':
            obj_ = ConceptosType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Conceptos = obj_
            obj_.original_tagname_ = 'Conceptos'
        elif nodeName_ == 'Impuestos':
            obj_ = ImpuestosType10.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Impuestos = obj_
            obj_.original_tagname_ = 'Impuestos'
        elif nodeName_ == 'Complemento':
            obj_ = ComplementoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Complemento = obj_
            obj_.original_tagname_ = 'Complemento'
        elif nodeName_ == 'Addenda':
            obj_ = AddendaType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Addenda = obj_
            obj_.original_tagname_ = 'Addenda'
# end class Comprobante

class InformacionGlobalType(GeneratedsSuper):
    """InformacionGlobalType -- Nodo condicional para precisar la informaci
    ??
    n relacionada con el comprobante global.
    Periodicidad -- Atributo requerido para expresar el per
    ??
    odo al que corresponde la informaci
    ??
    n del comprobante global.
    Meses -- Atributo requerido para expresar el mes o los meses al que corresponde la informaci
    ??
    n del comprobante global.
    A??o -- Atributo requerido para expresar el a
    ??
    o al que corresponde la informaci
    ??
    n del comprobante global.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Periodicidad=None, Meses=None, A??o=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Periodicidad = _cast(None, Periodicidad)
        self.Periodicidad_nsprefix_ = None
        self.Meses = _cast(None, Meses)
        self.Meses_nsprefix_ = None
        self.A??o = _cast(int, A??o)
        self.A??o_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InformacionGlobalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InformacionGlobalType.subclass:
            return InformacionGlobalType.subclass(*args_, **kwargs_)
        else:
            return InformacionGlobalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Periodicidad(self):
        return self.Periodicidad
    def set_Periodicidad(self, Periodicidad):
        self.Periodicidad = Periodicidad
    def get_Meses(self):
        return self.Meses
    def set_Meses(self, Meses):
        self.Meses = Meses
    def get_A??o(self):
        return self.A??o
    def set_A??o(self, A??o):
        self.A??o = A??o
    def validate_c_Periodicidad(self, value):
        # Validate type catCFDI:c_Periodicidad, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = ['01', '02', '03', '04', '05']
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_Periodicidad' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False
    def validate_c_Meses(self, value):
        # Validate type catCFDI:c_Meses, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_Meses' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_A??oType(self, value):
        # Validate type A??oType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 2021:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on A??oType' % {"value": value, "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='InformacionGlobalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InformacionGlobalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InformacionGlobalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InformacionGlobalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InformacionGlobalType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InformacionGlobalType'):
        if self.Periodicidad is not None and 'Periodicidad' not in already_processed:
            already_processed.add('Periodicidad')
            outfile.write(' Periodicidad=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Periodicidad), input_name='Periodicidad')), ))
        if self.Meses is not None and 'Meses' not in already_processed:
            already_processed.add('Meses')
            outfile.write(' Meses=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Meses), input_name='Meses')), ))
        if self.A??o is not None and 'A??o' not in already_processed:
            already_processed.add('A??o')
            outfile.write(' A??o="%s"' % self.gds_format_integer(self.A??o, input_name='A??o'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='InformacionGlobalType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Periodicidad', node)
        if value is not None and 'Periodicidad' not in already_processed:
            already_processed.add('Periodicidad')
            self.Periodicidad = value
            self.validate_c_Periodicidad(self.Periodicidad)    # validate type c_Periodicidad
        value = find_attr_value_('Meses', node)
        if value is not None and 'Meses' not in already_processed:
            already_processed.add('Meses')
            self.Meses = value
            self.validate_c_Meses(self.Meses)    # validate type c_Meses
        value = find_attr_value_('A??o', node)
        if value is not None and 'A??o' not in already_processed:
            already_processed.add('A??o')
            self.A??o = self.gds_parse_integer(value, node, 'A??o')
            self.validate_A??oType(self.A??o)    # validate type A??oType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class InformacionGlobalType

class CfdiRelacionadosType(GeneratedsSuper):
    """CfdiRelacionadosType -- Nodo opcional para precisar la informaci
    ??
    n de los comprobantes relacionados.
    TipoRelacion -- Atributo requerido para indicar la clave de la relaci
    ??
    n que existe entre
    ??
    ste que se est
    ??
    generando y el o los CFDI previos.
    CfdiRelacionado -- Nodo requerido para precisar la informaci
    ??
    n de los comprobantes relacionados.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TipoRelacion=None, CfdiRelacionado=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TipoRelacion = _cast(None, TipoRelacion)
        self.TipoRelacion_nsprefix_ = None
        if CfdiRelacionado is None:
            self.CfdiRelacionado = []
        else:
            self.CfdiRelacionado = CfdiRelacionado
        self.CfdiRelacionado_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CfdiRelacionadosType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CfdiRelacionadosType.subclass:
            return CfdiRelacionadosType.subclass(*args_, **kwargs_)
        else:
            return CfdiRelacionadosType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CfdiRelacionado(self):
        return self.CfdiRelacionado
    def set_CfdiRelacionado(self, CfdiRelacionado):
        self.CfdiRelacionado = CfdiRelacionado
    def add_CfdiRelacionado(self, value):
        self.CfdiRelacionado.append(value)
    def insert_CfdiRelacionado_at(self, index, value):
        self.CfdiRelacionado.insert(index, value)
    def replace_CfdiRelacionado_at(self, index, value):
        self.CfdiRelacionado[index] = value
    def get_TipoRelacion(self):
        return self.TipoRelacion
    def set_TipoRelacion(self, TipoRelacion):
        self.TipoRelacion = TipoRelacion
    def validate_c_TipoRelacion(self, value):
        # Validate type catCFDI:c_TipoRelacion, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_TipoRelacion' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            self.CfdiRelacionado
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='CfdiRelacionadosType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CfdiRelacionadosType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CfdiRelacionadosType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CfdiRelacionadosType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CfdiRelacionadosType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CfdiRelacionadosType'):
        if self.TipoRelacion is not None and 'TipoRelacion' not in already_processed:
            already_processed.add('TipoRelacion')
            outfile.write(' TipoRelacion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.TipoRelacion), input_name='TipoRelacion')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='CfdiRelacionadosType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for CfdiRelacionado_ in self.CfdiRelacionado:
            namespaceprefix_ = self.CfdiRelacionado_nsprefix_ + ':' if (UseCapturedNS_ and self.CfdiRelacionado_nsprefix_) else ''
            CfdiRelacionado_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CfdiRelacionado', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('TipoRelacion', node)
        if value is not None and 'TipoRelacion' not in already_processed:
            already_processed.add('TipoRelacion')
            self.TipoRelacion = value
            self.validate_c_TipoRelacion(self.TipoRelacion)    # validate type c_TipoRelacion
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CfdiRelacionado':
            obj_ = CfdiRelacionadoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CfdiRelacionado.append(obj_)
            obj_.original_tagname_ = 'CfdiRelacionado'
# end class CfdiRelacionadosType

class CfdiRelacionadoType(GeneratedsSuper):
    """CfdiRelacionadoType -- Nodo requerido para precisar la informaci
    ??
    n de los comprobantes relacionados.
    UUID -- Atributo requerido para registrar el folio fiscal (UUID) de un CFDI relacionado con el presente comprobante, por ejemplo: Si el CFDI relacionado es un comprobante de traslado que sirve para registrar el movimiento de la mercanc
    ??
    a. Si este comprobante se usa como nota de cr
    ??
    dito o nota de d
    ??
    bito del comprobante relacionado. Si este comprobante es una devoluci
    ??
    n sobre el comprobante relacionado. Si
    ??
    ste sustituye a una factura cancelada.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, UUID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.UUID = _cast(None, UUID)
        self.UUID_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CfdiRelacionadoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CfdiRelacionadoType.subclass:
            return CfdiRelacionadoType.subclass(*args_, **kwargs_)
        else:
            return CfdiRelacionadoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UUID(self):
        return self.UUID
    def set_UUID(self, UUID):
        self.UUID = UUID
    def validate_UUIDType(self, value):
        # Validate type UUIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 36:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on UUIDType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_UUIDType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_UUIDType_patterns_, ))
    validate_UUIDType_patterns_ = [['^([a-f0-9A-F]{8}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{12})$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='CfdiRelacionadoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CfdiRelacionadoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CfdiRelacionadoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CfdiRelacionadoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CfdiRelacionadoType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CfdiRelacionadoType'):
        if self.UUID is not None and 'UUID' not in already_processed:
            already_processed.add('UUID')
            outfile.write(' UUID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.UUID), input_name='UUID')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='CfdiRelacionadoType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('UUID', node)
        if value is not None and 'UUID' not in already_processed:
            already_processed.add('UUID')
            self.UUID = value
            self.validate_UUIDType(self.UUID)    # validate type UUIDType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CfdiRelacionadoType


class EmisorType(GeneratedsSuper):
    """EmisorType -- Nodo requerido para expresar la informaci
    ??
    n del contribuyente emisor del comprobante.
    Rfc -- Atributo requerido para registrar la Clave del Registro Federal de Contribuyentes correspondiente al contribuyente emisor del comprobante.
    Nombre -- Atributo requerido para registrar el nombre, denominaci
    ??
    n o raz
    ??
    n social del contribuyente inscrito en el RFC, del emisor del comprobante.
    RegimenFiscal -- Atributo requerido para incorporar la clave del r
    ??
    gimen del contribuyente emisor al que aplicar
    ??
    el efecto fiscal de este comprobante.
    FacAtrAdquirente -- Atributo condicional para expresar el n
    ??
    mero de operaci
    ??
    n proporcionado por el SAT cuando se trate de un comprobante a trav
    ??
    s de un PCECFDI o un PCGCFDISP.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Rfc=None, Nombre=None, RegimenFiscal=None, FacAtrAdquirente=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Rfc = _cast(None, Rfc)
        self.Rfc_nsprefix_ = None
        self.Nombre = _cast(None, Nombre)
        self.Nombre_nsprefix_ = None
        self.RegimenFiscal = _cast(None, RegimenFiscal)
        self.RegimenFiscal_nsprefix_ = None
        self.FacAtrAdquirente = _cast(None, FacAtrAdquirente)
        self.FacAtrAdquirente_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EmisorType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EmisorType.subclass:
            return EmisorType.subclass(*args_, **kwargs_)
        else:
            return EmisorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Rfc(self):
        return self.Rfc
    def set_Rfc(self, Rfc):
        self.Rfc = Rfc
    def get_Nombre(self):
        return self.Nombre
    def set_Nombre(self, Nombre):
        self.Nombre = Nombre
    def get_RegimenFiscal(self):
        return self.RegimenFiscal
    def set_RegimenFiscal(self, RegimenFiscal):
        self.RegimenFiscal = RegimenFiscal
    def get_FacAtrAdquirente(self):
        return self.FacAtrAdquirente
    def set_FacAtrAdquirente(self, FacAtrAdquirente):
        self.FacAtrAdquirente = FacAtrAdquirente
    def validate_t_RFC(self, value):
        # Validate type tdCFDI:t_RFC, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 13:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on t_RFC' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on t_RFC' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_RFC_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_RFC_patterns_, ))
    validate_t_RFC_patterns_ = [['^([A-Z&??]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A])$']]
    def validate_NombreType(self, value):
        # Validate type NombreType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 254:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NombreType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NombreType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NombreType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NombreType_patterns_, ))
    validate_NombreType_patterns_ = [['^([^|]{1,254})$']]
    def validate_c_RegimenFiscal(self, value):
        # Validate type catCFDI:c_RegimenFiscal, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['601', '603', '605', '606', '607', '608', '609', '610', '611', '612', '614', '615', '616', '620', '621', '622', '623', '624', '625', '626', '628', '629', '630']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_RegimenFiscal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_FacAtrAdquirenteType(self, value):
        # Validate type FacAtrAdquirenteType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on FacAtrAdquirenteType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_FacAtrAdquirenteType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_FacAtrAdquirenteType_patterns_, ))
    validate_FacAtrAdquirenteType_patterns_ = [['^([0-9]{10})$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='EmisorType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EmisorType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EmisorType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EmisorType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EmisorType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EmisorType'):
        if self.Rfc is not None and 'Rfc' not in already_processed:
            already_processed.add('Rfc')
            outfile.write(' Rfc=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Rfc), input_name='Rfc')), ))
        if self.Nombre is not None and 'Nombre' not in already_processed:
            already_processed.add('Nombre')
            outfile.write(' Nombre=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Nombre), input_name='Nombre')), ))
        if self.RegimenFiscal is not None and 'RegimenFiscal' not in already_processed:
            already_processed.add('RegimenFiscal')
            outfile.write(' RegimenFiscal=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.RegimenFiscal), input_name='RegimenFiscal')), ))
        if self.FacAtrAdquirente is not None and 'FacAtrAdquirente' not in already_processed:
            already_processed.add('FacAtrAdquirente')
            outfile.write(' FacAtrAdquirente=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.FacAtrAdquirente), input_name='FacAtrAdquirente')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='EmisorType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Rfc', node)
        if value is not None and 'Rfc' not in already_processed:
            already_processed.add('Rfc')
            self.Rfc = value
            self.validate_t_RFC(self.Rfc)    # validate type t_RFC
        value = find_attr_value_('Nombre', node)
        if value is not None and 'Nombre' not in already_processed:
            already_processed.add('Nombre')
            self.Nombre = value
            self.validate_NombreType(self.Nombre)    # validate type NombreType
        value = find_attr_value_('RegimenFiscal', node)
        if value is not None and 'RegimenFiscal' not in already_processed:
            already_processed.add('RegimenFiscal')
            self.RegimenFiscal = value
            self.validate_c_RegimenFiscal(self.RegimenFiscal)    # validate type c_RegimenFiscal
        value = find_attr_value_('FacAtrAdquirente', node)
        if value is not None and 'FacAtrAdquirente' not in already_processed:
            already_processed.add('FacAtrAdquirente')
            self.FacAtrAdquirente = value
            self.validate_FacAtrAdquirenteType(self.FacAtrAdquirente)    # validate type FacAtrAdquirenteType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class EmisorType


class ReceptorType(GeneratedsSuper):
    """ReceptorType -- Nodo requerido para precisar la informaci
    ??
    n del contribuyente receptor del comprobante.
    Rfc -- Atributo requerido para registrar la Clave del Registro Federal de Contribuyentes correspondiente al contribuyente receptor del comprobante.
    Nombre -- Atributo requerido para registrar el nombre(s), primer apellido, segundo apellido, seg
    ??
    n corresponda, denominaci
    ??
    n o raz
    ??
    n social del contribuyente, inscrito en el RFC, del receptor del comprobante.
    DomicilioFiscalReceptor -- Atributo requerido para registrar el c
    ??
    digo postal del domicilio fiscal del receptor del comprobante.
    ResidenciaFiscal -- Atributo condicional para registrar la clave del pa
    ??
    s de residencia para efectos fiscales del receptor del comprobante, cuando se trate de un extranjero, y que es conforme con la especificaci
    ??
    n ISO 3166-1 alpha-3. Es requerido cuando se incluya el complemento de comercio exterior o se registre el atributo NumRegIdTrib.
    NumRegIdTrib -- Atributo condicional para expresar el n
    ??
    mero de registro de identidad fiscal del receptor cuando sea residente en el extranjero. Es requerido cuando se incluya el complemento de comercio exterior.
    RegimenFiscalReceptor -- Atributo requerido para incorporar la clave del r
    ??
    gimen fiscal del contribuyente receptor al que aplicar
    ??
    el efecto fiscal de este comprobante.
    UsoCFDI -- Atributo requerido para expresar la clave del uso que dar
    ??
    a esta factura el receptor del CFDI.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Rfc=None, Nombre=None, DomicilioFiscalReceptor=None, ResidenciaFiscal=None, NumRegIdTrib=None, RegimenFiscalReceptor=None, UsoCFDI=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Rfc = _cast(None, Rfc)
        self.Rfc_nsprefix_ = None
        self.Nombre = _cast(None, Nombre)
        self.Nombre_nsprefix_ = None
        self.DomicilioFiscalReceptor = _cast(None, DomicilioFiscalReceptor)
        self.DomicilioFiscalReceptor_nsprefix_ = None
        self.ResidenciaFiscal = _cast(None, ResidenciaFiscal)
        self.ResidenciaFiscal_nsprefix_ = None
        self.NumRegIdTrib = _cast(None, NumRegIdTrib)
        self.NumRegIdTrib_nsprefix_ = None
        self.RegimenFiscalReceptor = _cast(None, RegimenFiscalReceptor)
        self.RegimenFiscalReceptor_nsprefix_ = None
        self.UsoCFDI = _cast(None, UsoCFDI)
        self.UsoCFDI_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReceptorType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReceptorType.subclass:
            return ReceptorType.subclass(*args_, **kwargs_)
        else:
            return ReceptorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Rfc(self):
        return self.Rfc
    def set_Rfc(self, Rfc):
        self.Rfc = Rfc
    def get_Nombre(self):
        return self.Nombre
    def set_Nombre(self, Nombre):
        self.Nombre = Nombre
    def get_DomicilioFiscalReceptor(self):
        return self.DomicilioFiscalReceptor
    def set_DomicilioFiscalReceptor(self, DomicilioFiscalReceptor):
        self.DomicilioFiscalReceptor = DomicilioFiscalReceptor
    def get_ResidenciaFiscal(self):
        return self.ResidenciaFiscal
    def set_ResidenciaFiscal(self, ResidenciaFiscal):
        self.ResidenciaFiscal = ResidenciaFiscal
    def get_NumRegIdTrib(self):
        return self.NumRegIdTrib
    def set_NumRegIdTrib(self, NumRegIdTrib):
        self.NumRegIdTrib = NumRegIdTrib
    def get_RegimenFiscalReceptor(self):
        return self.RegimenFiscalReceptor
    def set_RegimenFiscalReceptor(self, RegimenFiscalReceptor):
        self.RegimenFiscalReceptor = RegimenFiscalReceptor
    def get_UsoCFDI(self):
        return self.UsoCFDI
    def set_UsoCFDI(self, UsoCFDI):
        self.UsoCFDI = UsoCFDI
    def validate_t_RFC(self, value):
        # Validate type tdCFDI:t_RFC, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 13:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on t_RFC' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on t_RFC' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_RFC_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_RFC_patterns_, ))
    validate_t_RFC_patterns_ = [['^([A-Z&??]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A])$']]
    def validate_NombreType1(self, value):
        # Validate type NombreType1, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 254:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NombreType1' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NombreType1' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NombreType1_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NombreType1_patterns_, ))
    validate_NombreType1_patterns_ = [['^([^|]{1,254})$']]
    def validate_DomicilioFiscalReceptorType(self, value):
        # Validate type DomicilioFiscalReceptorType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on DomicilioFiscalReceptorType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_DomicilioFiscalReceptorType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_DomicilioFiscalReceptorType_patterns_, ))
    validate_DomicilioFiscalReceptorType_patterns_ = [['^([0-9]{5})$']]
    def validate_c_Pais(self, value):
        # Validate type catCFDI:c_Pais, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations =
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_Pais' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False
    def validate_NumRegIdTribType(self, value):
        # Validate type NumRegIdTribType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NumRegIdTribType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NumRegIdTribType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_c_RegimenFiscal(self, value):
        # Validate type catCFDI:c_RegimenFiscal, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['601', '603', '605', '606', '607', '608', '609', '610', '611', '612', '614', '615', '616', '620', '621', '622', '623', '624', '625', '626', '628', '629', '630']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_RegimenFiscal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_c_UsoCFDI(self, value):
        # Validate type catCFDI:c_UsoCFDI, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['G01', 'G02', 'G03', 'I01', 'I02', 'I03', 'I04', 'I05', 'I06', 'I07', 'I08', 'D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'P01', 'S01', 'CP01', 'CN01']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_UsoCFDI' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ReceptorType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReceptorType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReceptorType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReceptorType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReceptorType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ReceptorType'):
        if self.Rfc is not None and 'Rfc' not in already_processed:
            already_processed.add('Rfc')
            outfile.write(' Rfc=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Rfc), input_name='Rfc')), ))
        if self.Nombre is not None and 'Nombre' not in already_processed:
            already_processed.add('Nombre')
            outfile.write(' Nombre=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Nombre), input_name='Nombre')), ))
        if self.DomicilioFiscalReceptor is not None and 'DomicilioFiscalReceptor' not in already_processed:
            already_processed.add('DomicilioFiscalReceptor')
            outfile.write(' DomicilioFiscalReceptor=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.DomicilioFiscalReceptor), input_name='DomicilioFiscalReceptor')), ))
        if self.ResidenciaFiscal is not None and 'ResidenciaFiscal' not in already_processed:
            already_processed.add('ResidenciaFiscal')
            outfile.write(' ResidenciaFiscal=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ResidenciaFiscal), input_name='ResidenciaFiscal')), ))
        if self.NumRegIdTrib is not None and 'NumRegIdTrib' not in already_processed:
            already_processed.add('NumRegIdTrib')
            outfile.write(' NumRegIdTrib=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.NumRegIdTrib), input_name='NumRegIdTrib')), ))
        if self.RegimenFiscalReceptor is not None and 'RegimenFiscalReceptor' not in already_processed:
            already_processed.add('RegimenFiscalReceptor')
            outfile.write(' RegimenFiscalReceptor=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.RegimenFiscalReceptor), input_name='RegimenFiscalReceptor')), ))
        if self.UsoCFDI is not None and 'UsoCFDI' not in already_processed:
            already_processed.add('UsoCFDI')
            outfile.write(' UsoCFDI=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.UsoCFDI), input_name='UsoCFDI')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ReceptorType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Rfc', node)
        if value is not None and 'Rfc' not in already_processed:
            already_processed.add('Rfc')
            self.Rfc = value
            self.validate_t_RFC(self.Rfc)    # validate type t_RFC
        value = find_attr_value_('Nombre', node)
        if value is not None and 'Nombre' not in already_processed:
            already_processed.add('Nombre')
            self.Nombre = value
            self.validate_NombreType1(self.Nombre)    # validate type NombreType1
        value = find_attr_value_('DomicilioFiscalReceptor', node)
        if value is not None and 'DomicilioFiscalReceptor' not in already_processed:
            already_processed.add('DomicilioFiscalReceptor')
            self.DomicilioFiscalReceptor = value
            self.validate_DomicilioFiscalReceptorType(self.DomicilioFiscalReceptor)    # validate type DomicilioFiscalReceptorType
        value = find_attr_value_('ResidenciaFiscal', node)
        if value is not None and 'ResidenciaFiscal' not in already_processed:
            already_processed.add('ResidenciaFiscal')
            self.ResidenciaFiscal = value
            self.validate_c_Pais(self.ResidenciaFiscal)    # validate type c_Pais
        value = find_attr_value_('NumRegIdTrib', node)
        if value is not None and 'NumRegIdTrib' not in already_processed:
            already_processed.add('NumRegIdTrib')
            self.NumRegIdTrib = value
            self.validate_NumRegIdTribType(self.NumRegIdTrib)    # validate type NumRegIdTribType
        value = find_attr_value_('RegimenFiscalReceptor', node)
        if value is not None and 'RegimenFiscalReceptor' not in already_processed:
            already_processed.add('RegimenFiscalReceptor')
            self.RegimenFiscalReceptor = value
            self.validate_c_RegimenFiscal(self.RegimenFiscalReceptor)    # validate type c_RegimenFiscal
        value = find_attr_value_('UsoCFDI', node)
        if value is not None and 'UsoCFDI' not in already_processed:
            already_processed.add('UsoCFDI')
            self.UsoCFDI = value
            self.validate_c_UsoCFDI(self.UsoCFDI)    # validate type c_UsoCFDI
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ReceptorType


class ConceptosType(GeneratedsSuper):
    """ConceptosType -- Nodo requerido para listar los conceptos cubiertos por el comprobante.
    Concepto -- Nodo requerido para registrar la informaci
    ??
    n detallada de un bien o servicio amparado en el comprobante.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Concepto=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Concepto is None:
            self.Concepto = []
        else:
            self.Concepto = Concepto
        self.Concepto_nsprefix_ = 'cfdi'
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ConceptosType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ConceptosType.subclass:
            return ConceptosType.subclass(*args_, **kwargs_)
        else:
            return ConceptosType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Concepto(self):
        return self.Concepto
    def set_Concepto(self, Concepto):
        self.Concepto = Concepto
    def add_Concepto(self, value):
        self.Concepto.append(value)
    def insert_Concepto_at(self, index, value):
        self.Concepto.insert(index, value)
    def replace_Concepto_at(self, index, value):
        self.Concepto[index] = value
    def _hasContent(self):
        if (
            self.Concepto
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ConceptosType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ConceptosType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ConceptosType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ConceptosType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ConceptosType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ConceptosType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ConceptosType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Concepto_ in self.Concepto:
            namespaceprefix_ = self.Concepto_nsprefix_ + ':' if (UseCapturedNS_ and self.Concepto_nsprefix_) else ''
            Concepto_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Concepto', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Concepto':
            obj_ = ConceptoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Concepto.append(obj_)
            obj_.original_tagname_ = 'Concepto'
# end class ConceptosType


class ConceptoType(GeneratedsSuper):
    """ConceptoType -- Nodo requerido para registrar la informaci
    ??
    n detallada de un bien o servicio amparado en el comprobante.
    ClaveProdServ -- Atributo requerido para expresar la clave del producto o del servicio amparado por el presente concepto. Es requerido y deben utilizar las claves del cat
    ??
    logo de productos y servicios, cuando los conceptos que registren por sus actividades correspondan con dichos conceptos.
    NoIdentificacion -- Atributo opcional para expresar el n
    ??
    mero de parte, identificador del producto o del servicio, la clave de producto o servicio, SKU o equivalente, propia de la operaci
    ??
    n del emisor, amparado por el presente concepto. Opcionalmente se puede utilizar claves del est
    ??
    ndar GTIN.
    Cantidad -- Atributo requerido para precisar la cantidad de bienes o servicios del tipo particular definido por el presente concepto.
    ClaveUnidad -- Atributo requerido para precisar la clave de unidad de medida estandarizada aplicable para la cantidad expresada en el concepto. La unidad debe corresponder con la descripci
    ??
    n del concepto.
    Unidad -- Atributo opcional para precisar la unidad de medida propia de la operaci
    ??
    n del emisor, aplicable para la cantidad expresada en el concepto. La unidad debe corresponder con la descripci
    ??
    n del concepto.
    Descripcion -- Atributo requerido para precisar la descripci
    ??
    n del bien o servicio cubierto por el presente concepto.
    ValorUnitario -- Atributo requerido para precisar el valor o precio unitario del bien o servicio cubierto por el presente concepto.
    Importe -- Atributo requerido para precisar el importe total de los bienes o servicios del presente concepto. Debe ser equivalente al resultado de multiplicar la cantidad por el valor unitario expresado en el concepto. No se permiten valores negativos.
    Descuento -- Atributo opcional para representar el importe de los descuentos aplicables al concepto. No se permiten valores negativos.
    ObjetoImp -- Atributo requerido para expresar si la operaci
    ??
    n comercial es objeto o no de impuesto.
    Impuestos -- Nodo condicional para capturar los impuestos aplicables al presente concepto.
    ACuentaTerceros -- Nodo opcional para registrar informaci
    ??
    n del contribuyente Tercero, a cuenta del que se realiza la operaci
    ??
    n.
    InformacionAduanera -- Nodo opcional para introducir la informaci
    ??
    n aduanera aplicable cuando se trate de ventas de primera mano de mercanc
    ??
    as importadas o se trate de operaciones de comercio exterior con bienes o servicios.
    CuentaPredial -- Nodo opcional para asentar el n
    ??
    mero de cuenta predial con el que fue registrado el inmueble, en el sistema catastral de la entidad federativa de que trate, o bien para incorporar los datos de identificaci
    ??
    n del certificado de participaci
    ??
    n inmobiliaria no amortizable.
    ComplementoConcepto -- Nodo opcional donde se incluyen los nodos complementarios de extensi
    ??
    n al concepto definidos por el SAT, de acuerdo con las disposiciones particulares para un sector o actividad espec
    ??
    fica.
    Parte -- Nodo opcional para expresar las partes o componentes que integran la totalidad del concepto expresado en el comprobante fiscal digital por Internet.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ClaveProdServ=None, NoIdentificacion=None, Cantidad=None, ClaveUnidad=None, Unidad=None, Descripcion=None, ValorUnitario=None, Importe=None, Descuento=None, ObjetoImp=None, Impuestos=None, ACuentaTerceros=None, InformacionAduanera=None, CuentaPredial=None, ComplementoConcepto=None, Parte=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ClaveProdServ = _cast(None, ClaveProdServ)
        self.ClaveProdServ_nsprefix_ = None
        self.NoIdentificacion = _cast(None, NoIdentificacion)
        self.NoIdentificacion_nsprefix_ = None
        self.Cantidad = _cast(float, Cantidad)
        self.Cantidad_nsprefix_ = None
        self.ClaveUnidad = _cast(None, ClaveUnidad)
        self.ClaveUnidad_nsprefix_ = None
        self.Unidad = _cast(None, Unidad)
        self.Unidad_nsprefix_ = None
        self.Descripcion = _cast(None, Descripcion)
        self.Descripcion_nsprefix_ = None
        self.ValorUnitario = _cast(None, ValorUnitario)
        self.ValorUnitario_nsprefix_ = None
        self.Importe = _cast(None, Importe)
        self.Importe_nsprefix_ = None
        self.Descuento = _cast(None, Descuento)
        self.Descuento_nsprefix_ = None
        self.ObjetoImp = _cast(None, ObjetoImp)
        self.ObjetoImp_nsprefix_ = None
        self.Impuestos = Impuestos
        self.Impuestos_nsprefix_ = 'cfdi'
        self.ACuentaTerceros = ACuentaTerceros
        self.ACuentaTerceros_nsprefix_ = None
        if InformacionAduanera is None:
            self.InformacionAduanera = []
        else:
            self.InformacionAduanera = InformacionAduanera
        self.InformacionAduanera_nsprefix_ = 'cfdi'
        if CuentaPredial is None:
            self.CuentaPredial = []
        else:
            self.CuentaPredial = CuentaPredial
        self.CuentaPredial_nsprefix_ = None
        self.ComplementoConcepto = ComplementoConcepto
        self.ComplementoConcepto_nsprefix_ = 'cfdi'
        if Parte is None:
            self.Parte = []
        else:
            self.Parte = Parte
        self.Parte_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ConceptoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ConceptoType.subclass:
            return ConceptoType.subclass(*args_, **kwargs_)
        else:
            return ConceptoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Impuestos(self):
        return self.Impuestos
    def set_Impuestos(self, Impuestos):
        self.Impuestos = Impuestos
    def get_ACuentaTerceros(self):
        return self.ACuentaTerceros
    def set_ACuentaTerceros(self, ACuentaTerceros):
        self.ACuentaTerceros = ACuentaTerceros
    def get_InformacionAduanera(self):
        return self.InformacionAduanera
    def set_InformacionAduanera(self, InformacionAduanera):
        self.InformacionAduanera = InformacionAduanera
    def add_InformacionAduanera(self, value):
        self.InformacionAduanera.append(value)
    def insert_InformacionAduanera_at(self, index, value):
        self.InformacionAduanera.insert(index, value)
    def replace_InformacionAduanera_at(self, index, value):
        self.InformacionAduanera[index] = value
    def get_CuentaPredial(self):
        return self.CuentaPredial
    def set_CuentaPredial(self, CuentaPredial):
        self.CuentaPredial = CuentaPredial
    def add_CuentaPredial(self, value):
        self.CuentaPredial.append(value)
    def insert_CuentaPredial_at(self, index, value):
        self.CuentaPredial.insert(index, value)
    def replace_CuentaPredial_at(self, index, value):
        self.CuentaPredial[index] = value
    def get_ComplementoConcepto(self):
        return self.ComplementoConcepto
    def set_ComplementoConcepto(self, ComplementoConcepto):
        self.ComplementoConcepto = ComplementoConcepto
    def get_Parte(self):
        return self.Parte
    def set_Parte(self, Parte):
        self.Parte = Parte
    def add_Parte(self, value):
        self.Parte.append(value)
    def insert_Parte_at(self, index, value):
        self.Parte.insert(index, value)
    def replace_Parte_at(self, index, value):
        self.Parte[index] = value
    def get_ClaveProdServ(self):
        return self.ClaveProdServ
    def set_ClaveProdServ(self, ClaveProdServ):
        self.ClaveProdServ = ClaveProdServ
    def get_NoIdentificacion(self):
        return self.NoIdentificacion
    def set_NoIdentificacion(self, NoIdentificacion):
        self.NoIdentificacion = NoIdentificacion
    def get_Cantidad(self):
        return self.Cantidad
    def set_Cantidad(self, Cantidad):
        self.Cantidad = Cantidad
    def get_ClaveUnidad(self):
        return self.ClaveUnidad
    def set_ClaveUnidad(self, ClaveUnidad):
        self.ClaveUnidad = ClaveUnidad
    def get_Unidad(self):
        return self.Unidad
    def set_Unidad(self, Unidad):
        self.Unidad = Unidad
    def get_Descripcion(self):
        return self.Descripcion
    def set_Descripcion(self, Descripcion):
        self.Descripcion = Descripcion
    def get_ValorUnitario(self):
        return self.ValorUnitario
    def set_ValorUnitario(self, ValorUnitario):
        self.ValorUnitario = ValorUnitario
    def get_Importe(self):
        return self.Importe
    def set_Importe(self, Importe):
        self.Importe = Importe
    def get_Descuento(self):
        return self.Descuento
    def set_Descuento(self, Descuento):
        self.Descuento = Descuento
    def get_ObjetoImp(self):
        return self.ObjetoImp
    def set_ObjetoImp(self, ObjetoImp):
        self.ObjetoImp = ObjetoImp

    def validate_c_ClaveProdServ(self, value):
        # Validate type catCFDI:c_ClaveProdServ, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = 
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_ClaveProdServ' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False

    def validate_NoIdentificacionType6(self, value):
        # Validate type NoIdentificacionType6, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NoIdentificacionType6' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NoIdentificacionType6' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NoIdentificacionType6_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NoIdentificacionType6_patterns_, ))
    validate_NoIdentificacionType6_patterns_ = [['^([^|]{1,100})$']]
    def validate_CantidadType7(self, value):
        # Validate type CantidadType7, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000001:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on CantidadType7' % {"value": value, "lineno": lineno} )
                result = False
    def validate_c_ClaveUnidad(self, value):
        # Validate type catCFDI:c_ClaveUnidad, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = 
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_ClaveUnidad' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False

    def validate_UnidadType8(self, value):
        # Validate type UnidadType8, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on UnidadType8' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on UnidadType8' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_UnidadType8_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_UnidadType8_patterns_, ))
    validate_UnidadType8_patterns_ = [['^([^|]{1,20})$']]
    def validate_DescripcionType9(self, value):
        # Validate type DescripcionType9, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on DescripcionType9' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on DescripcionType9' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_DescripcionType9_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_DescripcionType9_patterns_, ))
    validate_DescripcionType9_patterns_ = [['^([^|]{1,1000})$']]
    def validate_t_Importe(self, value):
        # Validate type tdCFDI:t_Importe, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on t_Importe' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_Importe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_Importe_patterns_, ))
    validate_t_Importe_patterns_ = [['^([0-9]{1,18}(.[0-9]{1,6})?)$']]
    def validate_c_ObjetoImp(self, value):
        # Validate type catCFDI:c_ObjetoImp, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = ['01', '02', '03']
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_ObjetoImp' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False
    def _hasContent(self):
        if (
            self.Impuestos is not None or
            self.ACuentaTerceros is not None or
            self.InformacionAduanera or
            self.CuentaPredial or
            self.ComplementoConcepto is not None or
            self.Parte
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ConceptoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ConceptoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ConceptoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ConceptoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ConceptoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ConceptoType'):
        if self.ClaveProdServ is not None and 'ClaveProdServ' not in already_processed:
            already_processed.add('ClaveProdServ')
            outfile.write(' ClaveProdServ=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ClaveProdServ), input_name='ClaveProdServ')), ))
        if self.NoIdentificacion is not None and 'NoIdentificacion' not in already_processed:
            already_processed.add('NoIdentificacion')
            outfile.write(' NoIdentificacion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.NoIdentificacion), input_name='NoIdentificacion')), ))
        if self.Cantidad is not None and 'Cantidad' not in already_processed:
            already_processed.add('Cantidad')
            outfile.write(' Cantidad="%s"' % self.gds_format_decimal(self.Cantidad, input_name='Cantidad'))
        if self.ClaveUnidad is not None and 'ClaveUnidad' not in already_processed:
            already_processed.add('ClaveUnidad')
            outfile.write(' ClaveUnidad=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ClaveUnidad), input_name='ClaveUnidad')), ))
        if self.Unidad is not None and 'Unidad' not in already_processed:
            already_processed.add('Unidad')
            outfile.write(' Unidad=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Unidad), input_name='Unidad')), ))
        if self.Descripcion is not None and 'Descripcion' not in already_processed:
            already_processed.add('Descripcion')
            outfile.write(' Descripcion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Descripcion), input_name='Descripcion')), ))
        if self.ValorUnitario is not None and 'ValorUnitario' not in already_processed:
            already_processed.add('ValorUnitario')
            outfile.write(' ValorUnitario="%s"' % self.gds_format_decimal(self.ValorUnitario, input_name='ValorUnitario'))
        if self.Importe is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            outfile.write(' Importe="%s"' % self.gds_format_decimal(self.Importe, input_name='Importe'))
        if self.Descuento is not None and 'Descuento' not in already_processed:
            already_processed.add('Descuento')
            outfile.write(' Descuento="%s"' % self.gds_format_decimal(self.Descuento, input_name='Descuento'))
        if self.ObjetoImp is not None and 'ObjetoImp' not in already_processed:
            already_processed.add('ObjetoImp')
            outfile.write(' ObjetoImp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ObjetoImp), input_name='ObjetoImp')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ConceptoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Impuestos is not None:
            namespaceprefix_ = self.Impuestos_nsprefix_ + ':' if (UseCapturedNS_ and self.Impuestos_nsprefix_) else ''
            self.Impuestos.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Impuestos', pretty_print=pretty_print)
        if self.ACuentaTerceros is not None:
            namespaceprefix_ = self.ACuentaTerceros_nsprefix_ + ':' if (UseCapturedNS_ and self.ACuentaTerceros_nsprefix_) else ''
            self.ACuentaTerceros.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ACuentaTerceros', pretty_print=pretty_print)
        for InformacionAduanera_ in self.InformacionAduanera:
            namespaceprefix_ = self.InformacionAduanera_nsprefix_ + ':' if (UseCapturedNS_ and self.InformacionAduanera_nsprefix_) else ''
            InformacionAduanera_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InformacionAduanera', pretty_print=pretty_print)
        for CuentaPredial_ in self.CuentaPredial:
            namespaceprefix_ = self.CuentaPredial_nsprefix_ + ':' if (UseCapturedNS_ and self.CuentaPredial_nsprefix_) else ''
            CuentaPredial_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CuentaPredial', pretty_print=pretty_print)
        if self.ComplementoConcepto is not None:
            namespaceprefix_ = self.ComplementoConcepto_nsprefix_ + ':' if (UseCapturedNS_ and self.ComplementoConcepto_nsprefix_) else ''
            self.ComplementoConcepto.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ComplementoConcepto', pretty_print=pretty_print)
        for Parte_ in self.Parte:
            namespaceprefix_ = self.Parte_nsprefix_ + ':' if (UseCapturedNS_ and self.Parte_nsprefix_) else ''
            Parte_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Parte', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ClaveProdServ', node)
        if value is not None and 'ClaveProdServ' not in already_processed:
            already_processed.add('ClaveProdServ')
            self.ClaveProdServ = value
            self.validate_c_ClaveProdServ(self.ClaveProdServ)    # validate type c_ClaveProdServ
        value = find_attr_value_('NoIdentificacion', node)
        if value is not None and 'NoIdentificacion' not in already_processed:
            already_processed.add('NoIdentificacion')
            self.NoIdentificacion = value
            self.validate_NoIdentificacionType6(self.NoIdentificacion)    # validate type NoIdentificacionType6
        value = find_attr_value_('Cantidad', node)
        if value is not None and 'Cantidad' not in already_processed:
            already_processed.add('Cantidad')
            value = self.gds_parse_decimal(value, node, 'Cantidad')
            self.Cantidad = value
            self.validate_CantidadType7(self.Cantidad)    # validate type CantidadType7
        value = find_attr_value_('ClaveUnidad', node)
        if value is not None and 'ClaveUnidad' not in already_processed:
            already_processed.add('ClaveUnidad')
            self.ClaveUnidad = value
            self.validate_c_ClaveUnidad(self.ClaveUnidad)    # validate type c_ClaveUnidad
        value = find_attr_value_('Unidad', node)
        if value is not None and 'Unidad' not in already_processed:
            already_processed.add('Unidad')
            self.Unidad = value
            self.validate_UnidadType8(self.Unidad)    # validate type UnidadType8
        value = find_attr_value_('Descripcion', node)
        if value is not None and 'Descripcion' not in already_processed:
            already_processed.add('Descripcion')
            self.Descripcion = value
            self.validate_DescripcionType9(self.Descripcion)    # validate type DescripcionType9
        value = find_attr_value_('ValorUnitario', node)
        if value is not None and 'ValorUnitario' not in already_processed:
            already_processed.add('ValorUnitario')
            value = self.gds_parse_decimal(value, node, 'ValorUnitario')
            self.ValorUnitario = value
            self.validate_t_Importe(self.ValorUnitario)    # validate type t_Importe
        value = find_attr_value_('Importe', node)
        if value is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            value = self.gds_parse_decimal(value, node, 'Importe')
            self.Importe = value
            self.validate_t_Importe(self.Importe)    # validate type t_Importe
        value = find_attr_value_('Descuento', node)
        if value is not None and 'Descuento' not in already_processed:
            already_processed.add('Descuento')
            value = self.gds_parse_decimal(value, node, 'Descuento')
            self.Descuento = value
            self.validate_t_Importe(self.Descuento)    # validate type t_Importe
        value = find_attr_value_('ObjetoImp', node)
        if value is not None and 'ObjetoImp' not in already_processed:
            already_processed.add('ObjetoImp')
            self.ObjetoImp = value
            self.validate_c_ObjetoImp(self.ObjetoImp)    # validate type c_ObjetoImp
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Impuestos':
            obj_ = ImpuestosType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Impuestos = obj_
            obj_.original_tagname_ = 'Impuestos'
        elif nodeName_ == 'ACuentaTerceros':
            obj_ = ACuentaTercerosType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ACuentaTerceros = obj_
            obj_.original_tagname_ = 'ACuentaTerceros'
        elif nodeName_ == 'InformacionAduanera':
            obj_ = InformacionAduaneraType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InformacionAduanera.append(obj_)
            obj_.original_tagname_ = 'InformacionAduanera'
        elif nodeName_ == 'CuentaPredial':
            obj_ = CuentaPredialType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CuentaPredial.append(obj_)
            obj_.original_tagname_ = 'CuentaPredial'
        elif nodeName_ == 'ComplementoConcepto':
            obj_ = ComplementoConceptoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ComplementoConcepto = obj_
            obj_.original_tagname_ = 'ComplementoConcepto'
        elif nodeName_ == 'Parte':
            obj_ = ParteType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Parte.append(obj_)
            obj_.original_tagname_ = 'Parte'
# end class ConceptoType

class ImpuestosType(GeneratedsSuper):
    """ImpuestosType -- Nodo condicional para capturar los impuestos aplicables al presente concepto.
    Traslados -- Nodo opcional para asentar los impuestos trasladados aplicables al presente concepto.
    Retenciones -- Nodo opcional para asentar los impuestos retenidos aplicables al presente concepto.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Traslados=None, Retenciones=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Traslados = Traslados
        self.Traslados_nsprefix_ = 'cfdi'
        self.Retenciones = Retenciones
        self.Retenciones_nsprefix_ = 'cfdi'
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ImpuestosType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ImpuestosType.subclass:
            return ImpuestosType.subclass(*args_, **kwargs_)
        else:
            return ImpuestosType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Traslados(self):
        return self.Traslados
    def set_Traslados(self, Traslados):
        self.Traslados = Traslados
    def get_Retenciones(self):
        return self.Retenciones
    def set_Retenciones(self, Retenciones):
        self.Retenciones = Retenciones
    def _hasContent(self):
        if (
            self.Traslados is not None or
            self.Retenciones is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ImpuestosType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ImpuestosType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ImpuestosType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ImpuestosType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ImpuestosType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ImpuestosType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ImpuestosType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Traslados is not None:
            namespaceprefix_ = self.Traslados_nsprefix_ + ':' if (UseCapturedNS_ and self.Traslados_nsprefix_) else ''
            self.Traslados.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Traslados', pretty_print=pretty_print)
        if self.Retenciones is not None:
            namespaceprefix_ = self.Retenciones_nsprefix_ + ':' if (UseCapturedNS_ and self.Retenciones_nsprefix_) else ''
            self.Retenciones.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Retenciones', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Traslados':
            obj_ = TrasladosType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Traslados = obj_
            obj_.original_tagname_ = 'Traslados'
        elif nodeName_ == 'Retenciones':
            obj_ = RetencionesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Retenciones = obj_
            obj_.original_tagname_ = 'Retenciones'
# end class ImpuestosType

class TrasladosType(GeneratedsSuper):
    """TrasladosType -- Nodo opcional para asentar los impuestos trasladados aplicables al presente concepto.
    Traslado -- Nodo requerido para asentar la informaci
    ??
    n detallada de un traslado de impuestos aplicable al presente concepto.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Traslado=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Traslado is None:
            self.Traslado = []
        else:
            self.Traslado = Traslado
        self.Traslado_nsprefix_ = 'cfdi'
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrasladosType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrasladosType.subclass:
            return TrasladosType.subclass(*args_, **kwargs_)
        else:
            return TrasladosType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Traslado(self):
        return self.Traslado
    def set_Traslado(self, Traslado):
        self.Traslado = Traslado
    def add_Traslado(self, value):
        self.Traslado.append(value)
    def insert_Traslado_at(self, index, value):
        self.Traslado.insert(index, value)
    def replace_Traslado_at(self, index, value):
        self.Traslado[index] = value
    def _hasContent(self):
        if (
            self.Traslado
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='TrasladosType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrasladosType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TrasladosType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrasladosType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrasladosType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TrasladosType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='TrasladosType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Traslado_ in self.Traslado:
            namespaceprefix_ = self.Traslado_nsprefix_ + ':' if (UseCapturedNS_ and self.Traslado_nsprefix_) else ''
            Traslado_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Traslado', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Traslado':
            obj_ = TrasladoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Traslado.append(obj_)
            obj_.original_tagname_ = 'Traslado'
# end class TrasladosType

class TrasladoType(GeneratedsSuper):
    """TrasladoType -- Nodo requerido para asentar la informaci
    ??
    n detallada de un traslado de impuestos aplicable al presente concepto.
    Base -- Atributo requerido para se
    ??
    alar la base para el c
    ??
    lculo del impuesto, la determinaci
    ??
    n de la base se realiza de acuerdo con las disposiciones fiscales vigentes. No se permiten valores negativos.
    Impuesto -- Atributo requerido para se
    ??
    alar la clave del tipo de impuesto trasladado aplicable al concepto.
    TipoFactor -- Atributo requerido para se
    ??
    alar la clave del tipo de factor que se aplica a la base del impuesto.
    TasaOCuota -- Atributo condicional para se
    ??
    alar el valor de la tasa o cuota del impuesto que se traslada para el presente concepto. Es requerido cuando el atributo TipoFactor tenga una clave que corresponda a Tasa o Cuota.
    Importe -- Atributo condicional para se
    ??
    alar el importe del impuesto trasladado que aplica al concepto. No se permiten valores negativos. Es requerido cuando TipoFactor sea Tasa o Cuota.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Base=None, Impuesto=None, TipoFactor=None, TasaOCuota=None, Importe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Base = _cast(float, Base)
        self.Base_nsprefix_ = None
        self.Impuesto = _cast(None, Impuesto)
        self.Impuesto_nsprefix_ = None
        self.TipoFactor = _cast(None, TipoFactor)
        self.TipoFactor_nsprefix_ = None
        self.TasaOCuota = _cast(float, TasaOCuota)
        self.TasaOCuota_nsprefix_ = None
        self.Importe = _cast(None, Importe)
        self.Importe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrasladoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrasladoType.subclass:
            return TrasladoType.subclass(*args_, **kwargs_)
        else:
            return TrasladoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Base(self):
        return self.Base
    def set_Base(self, Base):
        self.Base = Base
    def get_Impuesto(self):
        return self.Impuesto
    def set_Impuesto(self, Impuesto):
        self.Impuesto = Impuesto
    def get_TipoFactor(self):
        return self.TipoFactor
    def set_TipoFactor(self, TipoFactor):
        self.TipoFactor = TipoFactor
    def get_TasaOCuota(self):
        return self.TasaOCuota
    def set_TasaOCuota(self, TasaOCuota):
        self.TasaOCuota = TasaOCuota
    def get_Importe(self):
        return self.Importe
    def set_Importe(self, Importe):
        self.Importe = Importe
    def validate_BaseType(self, value):
        # Validate type BaseType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000001:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on BaseType' % {"value": value, "lineno": lineno} )
                result = False
    def validate_c_Impuesto(self, value):
        # Validate type catCFDI:c_Impuesto, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = ['001', '002', '003']
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_Impuesto' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False

    def validate_c_TipoFactor(self, value):
        # Validate type catCFDI:c_TipoFactor, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Tasa', 'Cuota', 'Exento']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_TipoFactor' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TasaOCuotaType(self, value):
        # Validate type TasaOCuotaType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TasaOCuotaType' % {"value": value, "lineno": lineno} )
                result = False
    def validate_t_Importe(self, value):
        # Validate type tdCFDI:t_Importe, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on t_Importe' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_Importe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_Importe_patterns_, ))
    validate_t_Importe_patterns_ = [['^([0-9]{1,18}(.[0-9]{1,6})?)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='TrasladoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrasladoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TrasladoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrasladoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrasladoType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TrasladoType'):
        if self.Base is not None and 'Base' not in already_processed:
            already_processed.add('Base')
            outfile.write(' Base="%s"' % self.gds_format_decimal(self.Base, input_name='Base'))
        if self.Impuesto is not None and 'Impuesto' not in already_processed:
            already_processed.add('Impuesto')
            outfile.write(' Impuesto=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Impuesto), input_name='Impuesto')), ))
        if self.TipoFactor is not None and 'TipoFactor' not in already_processed:
            already_processed.add('TipoFactor')
            outfile.write(' TipoFactor=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.TipoFactor), input_name='TipoFactor')), ))
        if self.TasaOCuota is not None and 'TasaOCuota' not in already_processed:
            already_processed.add('TasaOCuota')
            outfile.write(' TasaOCuota="%s"' % self.gds_format_decimal(self.TasaOCuota, input_name='TasaOCuota'))
        if self.Importe is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            outfile.write(' Importe="%s"' % self.gds_format_decimal(self.Importe, input_name='Importe'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='TrasladoType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Base', node)
        if value is not None and 'Base' not in already_processed:
            already_processed.add('Base')
            value = self.gds_parse_decimal(value, node, 'Base')
            self.Base = value
            self.validate_BaseType(self.Base)    # validate type BaseType
        value = find_attr_value_('Impuesto', node)
        if value is not None and 'Impuesto' not in already_processed:
            already_processed.add('Impuesto')
            self.Impuesto = value
            self.validate_c_Impuesto(self.Impuesto)    # validate type c_Impuesto
        value = find_attr_value_('TipoFactor', node)
        if value is not None and 'TipoFactor' not in already_processed:
            already_processed.add('TipoFactor')
            self.TipoFactor = value
            self.validate_c_TipoFactor(self.TipoFactor)    # validate type c_TipoFactor
        value = find_attr_value_('TasaOCuota', node)
        if value is not None and 'TasaOCuota' not in already_processed:
            already_processed.add('TasaOCuota')
            value = self.gds_parse_decimal(value, node, 'TasaOCuota')
            self.TasaOCuota = value
            self.validate_TasaOCuotaType(self.TasaOCuota)    # validate type TasaOCuotaType
        value = find_attr_value_('Importe', node)
        if value is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            value = self.gds_parse_decimal(value, node, 'Importe')
            self.Importe = value
            self.validate_t_Importe(self.Importe)    # validate type t_Importe
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TrasladoType

class RetencionesType(GeneratedsSuper):
    """RetencionesType -- Nodo opcional para asentar los impuestos retenidos aplicables al presente concepto.
    Retencion -- Nodo requerido para asentar la informaci
    ??
    n detallada de una retenci
    ??
    n de impuestos aplicable al presente concepto.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Retencion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Retencion is None:
            self.Retencion = []
        else:
            self.Retencion = Retencion
        self.Retencion_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RetencionesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RetencionesType.subclass:
            return RetencionesType.subclass(*args_, **kwargs_)
        else:
            return RetencionesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Retencion(self):
        return self.Retencion
    def set_Retencion(self, Retencion):
        self.Retencion = Retencion
    def add_Retencion(self, value):
        self.Retencion.append(value)
    def insert_Retencion_at(self, index, value):
        self.Retencion.insert(index, value)
    def replace_Retencion_at(self, index, value):
        self.Retencion[index] = value
    def _hasContent(self):
        if (
            self.Retencion
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='RetencionesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RetencionesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RetencionesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RetencionesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RetencionesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RetencionesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='RetencionesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Retencion_ in self.Retencion:
            namespaceprefix_ = self.Retencion_nsprefix_ + ':' if (UseCapturedNS_ and self.Retencion_nsprefix_) else ''
            Retencion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Retencion', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Retencion':
            obj_ = RetencionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Retencion.append(obj_)
            obj_.original_tagname_ = 'Retencion'
# end class RetencionesType

class RetencionType(GeneratedsSuper):
    """RetencionType -- Nodo requerido para asentar la informaci
    ??
    n detallada de una retenci
    ??
    n de impuestos aplicable al presente concepto.
    Base -- Atributo requerido para se
    ??
    alar la base para el c
    ??
    lculo de la retenci
    ??
    n, la determinaci
    ??
    n de la base se realiza de acuerdo con las disposiciones fiscales vigentes. No se permiten valores negativos.
    Impuesto -- Atributo requerido para se
    ??
    alar la clave del tipo de impuesto retenido aplicable al concepto.
    TipoFactor -- Atributo requerido para se
    ??
    alar la clave del tipo de factor que se aplica a la base del impuesto.
    TasaOCuota -- Atributo requerido para se
    ??
    alar la tasa o cuota del impuesto que se retiene para el presente concepto.
    Importe -- Atributo requerido para se
    ??
    alar el importe del impuesto retenido que aplica al concepto. No se permiten valores negativos.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Base=None, Impuesto=None, TipoFactor=None, TasaOCuota=None, Importe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Base = _cast(float, Base)
        self.Base_nsprefix_ = None
        self.Impuesto = _cast(None, Impuesto)
        self.Impuesto_nsprefix_ = None
        self.TipoFactor = _cast(None, TipoFactor)
        self.TipoFactor_nsprefix_ = None
        self.TasaOCuota = _cast(float, TasaOCuota)
        self.TasaOCuota_nsprefix_ = None
        self.Importe = _cast(None, Importe)
        self.Importe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RetencionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RetencionType.subclass:
            return RetencionType.subclass(*args_, **kwargs_)
        else:
            return RetencionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Base(self):
        return self.Base
    def set_Base(self, Base):
        self.Base = Base
    def get_Impuesto(self):
        return self.Impuesto
    def set_Impuesto(self, Impuesto):
        self.Impuesto = Impuesto
    def get_TipoFactor(self):
        return self.TipoFactor
    def set_TipoFactor(self, TipoFactor):
        self.TipoFactor = TipoFactor
    def get_TasaOCuota(self):
        return self.TasaOCuota
    def set_TasaOCuota(self, TasaOCuota):
        self.TasaOCuota = TasaOCuota
    def get_Importe(self):
        return self.Importe
    def set_Importe(self, Importe):
        self.Importe = Importe
    def validate_BaseType2(self, value):
        # Validate type BaseType2, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000001:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on BaseType2' % {"value": value, "lineno": lineno} )
                result = False
    def validate_c_Impuesto(self, value):
        # Validate type catCFDI:c_Impuesto, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['001', '002', '003']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_Impuesto' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_c_TipoFactor(self, value):
        # Validate type catCFDI:c_TipoFactor, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Tasa', 'Cuota', 'Exento']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_TipoFactor' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TasaOCuotaType3(self, value):
        # Validate type TasaOCuotaType3, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TasaOCuotaType3' % {"value": value, "lineno": lineno} )
                result = False
    def validate_t_Importe(self, value):
        # Validate type tdCFDI:t_Importe, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on t_Importe' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_Importe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_Importe_patterns_, ))
    validate_t_Importe_patterns_ = [['^([0-9]{1,18}(.[0-9]{1,6})?)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='RetencionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RetencionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RetencionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RetencionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RetencionType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RetencionType'):
        if self.Base is not None and 'Base' not in already_processed:
            already_processed.add('Base')
            outfile.write(' Base="%s"' % self.gds_format_decimal(self.Base, input_name='Base'))
        if self.Impuesto is not None and 'Impuesto' not in already_processed:
            already_processed.add('Impuesto')
            outfile.write(' Impuesto=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Impuesto), input_name='Impuesto')), ))
        if self.TipoFactor is not None and 'TipoFactor' not in already_processed:
            already_processed.add('TipoFactor')
            outfile.write(' TipoFactor=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.TipoFactor), input_name='TipoFactor')), ))
        if self.TasaOCuota is not None and 'TasaOCuota' not in already_processed:
            already_processed.add('TasaOCuota')
            outfile.write(' TasaOCuota="%s"' % self.gds_format_decimal(self.TasaOCuota, input_name='TasaOCuota'))
        if self.Importe is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            outfile.write(' Importe="%s"' % self.gds_format_decimal(self.Importe, input_name='Importe'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='RetencionType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Base', node)
        if value is not None and 'Base' not in already_processed:
            already_processed.add('Base')
            value = self.gds_parse_decimal(value, node, 'Base')
            self.Base = value
            self.validate_BaseType2(self.Base)    # validate type BaseType2
        value = find_attr_value_('Impuesto', node)
        if value is not None and 'Impuesto' not in already_processed:
            already_processed.add('Impuesto')
            self.Impuesto = value
            self.validate_c_Impuesto(self.Impuesto)    # validate type c_Impuesto
        value = find_attr_value_('TipoFactor', node)
        if value is not None and 'TipoFactor' not in already_processed:
            already_processed.add('TipoFactor')
            self.TipoFactor = value
            self.validate_c_TipoFactor(self.TipoFactor)    # validate type c_TipoFactor
        value = find_attr_value_('TasaOCuota', node)
        if value is not None and 'TasaOCuota' not in already_processed:
            already_processed.add('TasaOCuota')
            value = self.gds_parse_decimal(value, node, 'TasaOCuota')
            self.TasaOCuota = value
            self.validate_TasaOCuotaType3(self.TasaOCuota)    # validate type TasaOCuotaType3
        value = find_attr_value_('Importe', node)
        if value is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            value = self.gds_parse_decimal(value, node, 'Importe')
            self.Importe = value
            self.validate_t_Importe(self.Importe)    # validate type t_Importe
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RetencionType

class ACuentaTercerosType(GeneratedsSuper):
    """ACuentaTercerosType -- Nodo opcional para registrar informaci
    ??
    n del contribuyente Tercero, a cuenta del que se realiza la operaci
    ??
    n.
    RfcACuentaTerceros -- Atributo requerido para registrar la Clave del Registro Federal de Contribuyentes del contribuyente Tercero, a cuenta del que se realiza la operaci
    ??
    n.
    NombreACuentaTerceros -- Atributo requerido para registrar el nombre, denominaci
    ??
    n o raz
    ??
    n social del contribuyente Tercero correspondiente con el Rfc, a cuenta del que se realiza la operaci
    ??
    n.
    RegimenFiscalACuentaTerceros -- Atributo requerido para incorporar la clave del r
    ??
    gimen del contribuyente Tercero, a cuenta del que se realiza la operaci
    ??
    n.
    DomicilioFiscalACuentaTerceros -- Atributo requerido para incorporar el c
    ??
    digo postal del domicilio fiscal del Tercero, a cuenta del que se realiza la operaci
    ??
    n.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, RfcACuentaTerceros=None, NombreACuentaTerceros=None, RegimenFiscalACuentaTerceros=None, DomicilioFiscalACuentaTerceros=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.RfcACuentaTerceros = _cast(None, RfcACuentaTerceros)
        self.RfcACuentaTerceros_nsprefix_ = None
        self.NombreACuentaTerceros = _cast(None, NombreACuentaTerceros)
        self.NombreACuentaTerceros_nsprefix_ = None
        self.RegimenFiscalACuentaTerceros = _cast(None, RegimenFiscalACuentaTerceros)
        self.RegimenFiscalACuentaTerceros_nsprefix_ = None
        self.DomicilioFiscalACuentaTerceros = _cast(None, DomicilioFiscalACuentaTerceros)
        self.DomicilioFiscalACuentaTerceros_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ACuentaTercerosType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ACuentaTercerosType.subclass:
            return ACuentaTercerosType.subclass(*args_, **kwargs_)
        else:
            return ACuentaTercerosType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_RfcACuentaTerceros(self):
        return self.RfcACuentaTerceros
    def set_RfcACuentaTerceros(self, RfcACuentaTerceros):
        self.RfcACuentaTerceros = RfcACuentaTerceros
    def get_NombreACuentaTerceros(self):
        return self.NombreACuentaTerceros
    def set_NombreACuentaTerceros(self, NombreACuentaTerceros):
        self.NombreACuentaTerceros = NombreACuentaTerceros
    def get_RegimenFiscalACuentaTerceros(self):
        return self.RegimenFiscalACuentaTerceros
    def set_RegimenFiscalACuentaTerceros(self, RegimenFiscalACuentaTerceros):
        self.RegimenFiscalACuentaTerceros = RegimenFiscalACuentaTerceros
    def get_DomicilioFiscalACuentaTerceros(self):
        return self.DomicilioFiscalACuentaTerceros
    def set_DomicilioFiscalACuentaTerceros(self, DomicilioFiscalACuentaTerceros):
        self.DomicilioFiscalACuentaTerceros = DomicilioFiscalACuentaTerceros
    def validate_t_RFC(self, value):
        # Validate type tdCFDI:t_RFC, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 13:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on t_RFC' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on t_RFC' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_RFC_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_RFC_patterns_, ))
    validate_t_RFC_patterns_ = [['^([A-Z&??]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A])$']]
    def validate_NombreACuentaTercerosType(self, value):
        # Validate type NombreACuentaTercerosType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 254:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NombreACuentaTercerosType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NombreACuentaTercerosType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NombreACuentaTercerosType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NombreACuentaTercerosType_patterns_, ))
    validate_NombreACuentaTercerosType_patterns_ = [['^([^|]{1,254})$']]
    def validate_c_RegimenFiscal(self, value):
        # Validate type catCFDI:c_RegimenFiscal, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['601', '603', '605', '606', '607', '608', '609', '610', '611', '612', '614', '615', '616', '620', '621', '622', '623', '624', '625', '626', '628', '629', '630']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_RegimenFiscal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_DomicilioFiscalACuentaTercerosType(self, value):
        # Validate type DomicilioFiscalACuentaTercerosType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on DomicilioFiscalACuentaTercerosType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_DomicilioFiscalACuentaTercerosType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_DomicilioFiscalACuentaTercerosType_patterns_, ))
    validate_DomicilioFiscalACuentaTercerosType_patterns_ = [['^([0-9]{5})$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ACuentaTercerosType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ACuentaTercerosType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ACuentaTercerosType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ACuentaTercerosType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ACuentaTercerosType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ACuentaTercerosType'):
        if self.RfcACuentaTerceros is not None and 'RfcACuentaTerceros' not in already_processed:
            already_processed.add('RfcACuentaTerceros')
            outfile.write(' RfcACuentaTerceros=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.RfcACuentaTerceros), input_name='RfcACuentaTerceros')), ))
        if self.NombreACuentaTerceros is not None and 'NombreACuentaTerceros' not in already_processed:
            already_processed.add('NombreACuentaTerceros')
            outfile.write(' NombreACuentaTerceros=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.NombreACuentaTerceros), input_name='NombreACuentaTerceros')), ))
        if self.RegimenFiscalACuentaTerceros is not None and 'RegimenFiscalACuentaTerceros' not in already_processed:
            already_processed.add('RegimenFiscalACuentaTerceros')
            outfile.write(' RegimenFiscalACuentaTerceros=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.RegimenFiscalACuentaTerceros), input_name='RegimenFiscalACuentaTerceros')), ))
        if self.DomicilioFiscalACuentaTerceros is not None and 'DomicilioFiscalACuentaTerceros' not in already_processed:
            already_processed.add('DomicilioFiscalACuentaTerceros')
            outfile.write(' DomicilioFiscalACuentaTerceros=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.DomicilioFiscalACuentaTerceros), input_name='DomicilioFiscalACuentaTerceros')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ACuentaTercerosType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('RfcACuentaTerceros', node)
        if value is not None and 'RfcACuentaTerceros' not in already_processed:
            already_processed.add('RfcACuentaTerceros')
            self.RfcACuentaTerceros = value
            self.validate_t_RFC(self.RfcACuentaTerceros)    # validate type t_RFC
        value = find_attr_value_('NombreACuentaTerceros', node)
        if value is not None and 'NombreACuentaTerceros' not in already_processed:
            already_processed.add('NombreACuentaTerceros')
            self.NombreACuentaTerceros = value
            self.validate_NombreACuentaTercerosType(self.NombreACuentaTerceros)    # validate type NombreACuentaTercerosType
        value = find_attr_value_('RegimenFiscalACuentaTerceros', node)
        if value is not None and 'RegimenFiscalACuentaTerceros' not in already_processed:
            already_processed.add('RegimenFiscalACuentaTerceros')
            self.RegimenFiscalACuentaTerceros = value
            self.validate_c_RegimenFiscal(self.RegimenFiscalACuentaTerceros)    # validate type c_RegimenFiscal
        value = find_attr_value_('DomicilioFiscalACuentaTerceros', node)
        if value is not None and 'DomicilioFiscalACuentaTerceros' not in already_processed:
            already_processed.add('DomicilioFiscalACuentaTerceros')
            self.DomicilioFiscalACuentaTerceros = value
            self.validate_DomicilioFiscalACuentaTercerosType(self.DomicilioFiscalACuentaTerceros)    # validate type DomicilioFiscalACuentaTercerosType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ACuentaTercerosType


class InformacionAduaneraType(GeneratedsSuper):
    """InformacionAduaneraType -- Nodo opcional para introducir la informaci
    ??
    n aduanera aplicable cuando se trate de ventas de primera mano de mercanc
    ??
    as importadas o se trate de operaciones de comercio exterior con bienes o servicios.
    NumeroPedimento -- Atributo requerido para expresar el n
    ??
    mero del pedimento que ampara la importaci
    ??
    n del bien que se expresa en el siguiente formato:
    ??
    ltimos 2 d
    ??
    gitos del a
    ??
    o de validaci
    ??
    n seguidos por dos espacios, 2 d
    ??
    gitos de la aduana de despacho seguidos por dos espacios, 4 d
    ??
    gitos del n
    ??
    mero de la patente seguidos por dos espacios, 1 d
    ??
    gito que corresponde al
    ??
    ltimo d
    ??
    gito del a
    ??
    o en curso, salvo que se trate de un pedimento consolidado iniciado en el a
    ??
    o inmediato anterior o del pedimento original de una rectificaci
    ??
    n, seguido de 6 d
    ??
    gitos de la numeraci
    ??
    n progresiva por aduana.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, NumeroPedimento=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.NumeroPedimento = _cast(None, NumeroPedimento)
        self.NumeroPedimento_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InformacionAduaneraType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InformacionAduaneraType.subclass:
            return InformacionAduaneraType.subclass(*args_, **kwargs_)
        else:
            return InformacionAduaneraType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_NumeroPedimento(self):
        return self.NumeroPedimento
    def set_NumeroPedimento(self, NumeroPedimento):
        self.NumeroPedimento = NumeroPedimento
    def validate_NumeroPedimentoType(self, value):
        # Validate type NumeroPedimentoType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on NumeroPedimentoType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NumeroPedimentoType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NumeroPedimentoType_patterns_, ))
    validate_NumeroPedimentoType_patterns_ = [['^([0-9]{2}  [0-9]{2}  [0-9]{4}  [0-9]{7})$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='InformacionAduaneraType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InformacionAduaneraType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InformacionAduaneraType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InformacionAduaneraType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InformacionAduaneraType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InformacionAduaneraType'):
        if self.NumeroPedimento is not None and 'NumeroPedimento' not in already_processed:
            already_processed.add('NumeroPedimento')
            outfile.write(' NumeroPedimento=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.NumeroPedimento), input_name='NumeroPedimento')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='InformacionAduaneraType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('NumeroPedimento', node)
        if value is not None and 'NumeroPedimento' not in already_processed:
            already_processed.add('NumeroPedimento')
            self.NumeroPedimento = value
            self.validate_NumeroPedimentoType(self.NumeroPedimento)    # validate type NumeroPedimentoType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class InformacionAduaneraType


class CuentaPredialType(GeneratedsSuper):
    """CuentaPredialType -- Nodo opcional para asentar el n
    ??
    mero de cuenta predial con el que fue registrado el inmueble, en el sistema catastral de la entidad federativa de que trate, o bien para incorporar los datos de identificaci
    ??
    n del certificado de participaci
    ??
    n inmobiliaria no amortizable.
    Numero -- Atributo requerido para precisar el n
    ??
    mero de la cuenta predial del inmueble cubierto por el presente concepto, o bien para incorporar los datos de identificaci
    ??
    n del certificado de participaci
    ??
    n inmobiliaria no amortizable, trat
    ??
    ndose de arrendamiento.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Numero=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Numero = _cast(None, Numero)
        self.Numero_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CuentaPredialType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CuentaPredialType.subclass:
            return CuentaPredialType.subclass(*args_, **kwargs_)
        else:
            return CuentaPredialType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Numero(self):
        return self.Numero
    def set_Numero(self, Numero):
        self.Numero = Numero
    def validate_NumeroType(self, value):
        # Validate type NumeroType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 150:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NumeroType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NumeroType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NumeroType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NumeroType_patterns_, ))
    validate_NumeroType_patterns_ = [['^([0-9a-zA-Z]{1,150})$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='CuentaPredialType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CuentaPredialType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CuentaPredialType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CuentaPredialType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CuentaPredialType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CuentaPredialType'):
        if self.Numero is not None and 'Numero' not in already_processed:
            already_processed.add('Numero')
            outfile.write(' Numero=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Numero), input_name='Numero')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='CuentaPredialType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Numero', node)
        if value is not None and 'Numero' not in already_processed:
            already_processed.add('Numero')
            self.Numero = value
            self.validate_NumeroType(self.Numero)    # validate type NumeroType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CuentaPredialType


class ComplementoConceptoType(GeneratedsSuper):
    """ComplementoConceptoType -- Nodo opcional donde se incluyen los nodos complementarios de extensi
    ??
    n al concepto definidos por el SAT, de acuerdo con las disposiciones particulares para un sector o actividad espec
    ??
    fica.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ComplementoConceptoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ComplementoConceptoType.subclass:
            return ComplementoConceptoType.subclass(*args_, **kwargs_)
        else:
            return ComplementoConceptoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def _hasContent(self):
        if (
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ComplementoConceptoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ComplementoConceptoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ComplementoConceptoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ComplementoConceptoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ComplementoConceptoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ComplementoConceptoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ComplementoConceptoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        content_ = self.gds_build_any(child_, 'ComplementoConceptoType')
        self.anytypeobjs_.append(content_)
# end class ComplementoConceptoType


class ParteType(GeneratedsSuper):
    """ParteType -- Nodo opcional para expresar las partes o componentes que integran la totalidad del concepto expresado en el comprobante fiscal digital por Internet.
    ClaveProdServ -- Atributo requerido para expresar la clave del producto o del servicio amparado por la presente parte. Es requerido y deben utilizar las claves del cat
    ??
    logo de productos y servicios, cuando los conceptos que registren por sus actividades correspondan con dichos conceptos.
    NoIdentificacion -- Atributo opcional para expresar el n
    ??
    mero de serie, n
    ??
    mero de parte del bien o identificador del producto o del servicio amparado por la presente parte. Opcionalmente se puede utilizar claves del est
    ??
    ndar GTIN.
    Cantidad -- Atributo requerido para precisar la cantidad de bienes o servicios del tipo particular definido por la presente parte.
    Unidad -- Atributo opcional para precisar la unidad de medida propia de la operaci
    ??
    n del emisor, aplicable para la cantidad expresada en la parte. La unidad debe corresponder con la descripci
    ??
    n de la parte.
    Descripcion -- Atributo requerido para precisar la descripci
    ??
    n del bien o servicio cubierto por la presente parte.
    ValorUnitario -- Atributo opcional para precisar el valor o precio unitario del bien o servicio cubierto por la presente parte. No se permiten valores negativos.
    Importe -- Atributo opcional para precisar el importe total de los bienes o servicios de la presente parte. Debe ser equivalente al resultado de multiplicar la cantidad por el valor unitario expresado en la parte. No se permiten valores negativos.
    InformacionAduanera -- Nodo opcional para introducir la informaci
    ??
    n aduanera aplicable cuando se trate de ventas de primera mano de mercanc
    ??
    as importadas o se trate de operaciones de comercio exterior con bienes o servicios.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ClaveProdServ=None, NoIdentificacion=None, Cantidad=None, Unidad=None, Descripcion=None, ValorUnitario=None, Importe=None, InformacionAduanera=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ClaveProdServ = _cast(None, ClaveProdServ)
        self.ClaveProdServ_nsprefix_ = None
        self.NoIdentificacion = _cast(None, NoIdentificacion)
        self.NoIdentificacion_nsprefix_ = None
        self.Cantidad = _cast(float, Cantidad)
        self.Cantidad_nsprefix_ = None
        self.Unidad = _cast(None, Unidad)
        self.Unidad_nsprefix_ = None
        self.Descripcion = _cast(None, Descripcion)
        self.Descripcion_nsprefix_ = None
        self.ValorUnitario = _cast(None, ValorUnitario)
        self.ValorUnitario_nsprefix_ = None
        self.Importe = _cast(None, Importe)
        self.Importe_nsprefix_ = None
        if InformacionAduanera is None:
            self.InformacionAduanera = []
        else:
            self.InformacionAduanera = InformacionAduanera
        self.InformacionAduanera_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParteType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParteType.subclass:
            return ParteType.subclass(*args_, **kwargs_)
        else:
            return ParteType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_InformacionAduanera(self):
        return self.InformacionAduanera
    def set_InformacionAduanera(self, InformacionAduanera):
        self.InformacionAduanera = InformacionAduanera
    def add_InformacionAduanera(self, value):
        self.InformacionAduanera.append(value)
    def insert_InformacionAduanera_at(self, index, value):
        self.InformacionAduanera.insert(index, value)
    def replace_InformacionAduanera_at(self, index, value):
        self.InformacionAduanera[index] = value
    def get_ClaveProdServ(self):
        return self.ClaveProdServ
    def set_ClaveProdServ(self, ClaveProdServ):
        self.ClaveProdServ = ClaveProdServ
    def get_NoIdentificacion(self):
        return self.NoIdentificacion
    def set_NoIdentificacion(self, NoIdentificacion):
        self.NoIdentificacion = NoIdentificacion
    def get_Cantidad(self):
        return self.Cantidad
    def set_Cantidad(self, Cantidad):
        self.Cantidad = Cantidad
    def get_Unidad(self):
        return self.Unidad
    def set_Unidad(self, Unidad):
        self.Unidad = Unidad
    def get_Descripcion(self):
        return self.Descripcion
    def set_Descripcion(self, Descripcion):
        self.Descripcion = Descripcion
    def get_ValorUnitario(self):
        return self.ValorUnitario
    def set_ValorUnitario(self, ValorUnitario):
        self.ValorUnitario = ValorUnitario
    def get_Importe(self):
        return self.Importe
    def set_Importe(self, Importe):
        self.Importe = Importe

    def validate_c_ClaveProdServ(self, value):
        # Validate type catCFDI:c_ClaveProdServ, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            # enumerations = 
            # if value not in enumerations:
            #     lineno = self.gds_get_node_lineno_()
            #     self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_ClaveProdServ' % {"value" : encode_str_2_3(value), "lineno": lineno} )
            #     result = False

    def validate_NoIdentificacionType(self, value):
        # Validate type NoIdentificacionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NoIdentificacionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NoIdentificacionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NoIdentificacionType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NoIdentificacionType_patterns_, ))
    validate_NoIdentificacionType_patterns_ = [['^([^|]{1,100})$']]
    def validate_CantidadType(self, value):
        # Validate type CantidadType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000001:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on CantidadType' % {"value": value, "lineno": lineno} )
                result = False
    def validate_UnidadType(self, value):
        # Validate type UnidadType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on UnidadType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on UnidadType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_UnidadType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_UnidadType_patterns_, ))
    validate_UnidadType_patterns_ = [['^([^|]{1,20})$']]
    def validate_DescripcionType(self, value):
        # Validate type DescripcionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on DescripcionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on DescripcionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_DescripcionType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_DescripcionType_patterns_, ))
    validate_DescripcionType_patterns_ = [['^([^|]{1,1000})$']]
    def validate_t_Importe(self, value):
        # Validate type tdCFDI:t_Importe, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on t_Importe' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_Importe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_Importe_patterns_, ))
    validate_t_Importe_patterns_ = [['^([0-9]{1,18}(.[0-9]{1,6})?)$']]
    def _hasContent(self):
        if (
            self.InformacionAduanera
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ParteType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParteType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParteType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParteType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParteType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParteType'):
        if self.ClaveProdServ is not None and 'ClaveProdServ' not in already_processed:
            already_processed.add('ClaveProdServ')
            outfile.write(' ClaveProdServ=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ClaveProdServ), input_name='ClaveProdServ')), ))
        if self.NoIdentificacion is not None and 'NoIdentificacion' not in already_processed:
            already_processed.add('NoIdentificacion')
            outfile.write(' NoIdentificacion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.NoIdentificacion), input_name='NoIdentificacion')), ))
        if self.Cantidad is not None and 'Cantidad' not in already_processed:
            already_processed.add('Cantidad')
            outfile.write(' Cantidad="%s"' % self.gds_format_decimal(self.Cantidad, input_name='Cantidad'))
        if self.Unidad is not None and 'Unidad' not in already_processed:
            already_processed.add('Unidad')
            outfile.write(' Unidad=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Unidad), input_name='Unidad')), ))
        if self.Descripcion is not None and 'Descripcion' not in already_processed:
            already_processed.add('Descripcion')
            outfile.write(' Descripcion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Descripcion), input_name='Descripcion')), ))
        if self.ValorUnitario is not None and 'ValorUnitario' not in already_processed:
            already_processed.add('ValorUnitario')
            outfile.write(' ValorUnitario="%s"' % self.gds_format_decimal(self.ValorUnitario, input_name='ValorUnitario'))
        if self.Importe is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            outfile.write(' Importe="%s"' % self.gds_format_decimal(self.Importe, input_name='Importe'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ParteType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for InformacionAduanera_ in self.InformacionAduanera:
            namespaceprefix_ = self.InformacionAduanera_nsprefix_ + ':' if (UseCapturedNS_ and self.InformacionAduanera_nsprefix_) else ''
            InformacionAduanera_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InformacionAduanera', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ClaveProdServ', node)
        if value is not None and 'ClaveProdServ' not in already_processed:
            already_processed.add('ClaveProdServ')
            self.ClaveProdServ = value
            self.validate_c_ClaveProdServ(self.ClaveProdServ)    # validate type c_ClaveProdServ
        value = find_attr_value_('NoIdentificacion', node)
        if value is not None and 'NoIdentificacion' not in already_processed:
            already_processed.add('NoIdentificacion')
            self.NoIdentificacion = value
            self.validate_NoIdentificacionType(self.NoIdentificacion)    # validate type NoIdentificacionType
        value = find_attr_value_('Cantidad', node)
        if value is not None and 'Cantidad' not in already_processed:
            already_processed.add('Cantidad')
            value = self.gds_parse_decimal(value, node, 'Cantidad')
            self.Cantidad = value
            self.validate_CantidadType(self.Cantidad)    # validate type CantidadType
        value = find_attr_value_('Unidad', node)
        if value is not None and 'Unidad' not in already_processed:
            already_processed.add('Unidad')
            self.Unidad = value
            self.validate_UnidadType(self.Unidad)    # validate type UnidadType
        value = find_attr_value_('Descripcion', node)
        if value is not None and 'Descripcion' not in already_processed:
            already_processed.add('Descripcion')
            self.Descripcion = value
            self.validate_DescripcionType(self.Descripcion)    # validate type DescripcionType
        value = find_attr_value_('ValorUnitario', node)
        if value is not None and 'ValorUnitario' not in already_processed:
            already_processed.add('ValorUnitario')
            value = self.gds_parse_decimal(value, node, 'ValorUnitario')
            self.ValorUnitario = value
            self.validate_t_Importe(self.ValorUnitario)    # validate type t_Importe
        value = find_attr_value_('Importe', node)
        if value is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            value = self.gds_parse_decimal(value, node, 'Importe')
            self.Importe = value
            self.validate_t_Importe(self.Importe)    # validate type t_Importe
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InformacionAduanera':
            obj_ = InformacionAduaneraType4.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InformacionAduanera.append(obj_)
            obj_.original_tagname_ = 'InformacionAduanera'
# end class ParteType


class InformacionAduaneraType4(GeneratedsSuper):
    """InformacionAduaneraType4 -- Nodo opcional para introducir la informaci
    ??
    n aduanera aplicable cuando se trate de ventas de primera mano de mercanc
    ??
    as importadas o se trate de operaciones de comercio exterior con bienes o servicios.
    NumeroPedimento -- Atributo requerido para expresar el n
    ??
    mero del pedimento que ampara la importaci
    ??
    n del bien que se expresa en el siguiente formato:
    ??
    ltimos 2 d
    ??
    gitos del a
    ??
    o de validaci
    ??
    n seguidos por dos espacios, 2 d
    ??
    gitos de la aduana de despacho seguidos por dos espacios, 4 d
    ??
    gitos del n
    ??
    mero de la patente seguidos por dos espacios, 1 d
    ??
    gito que corresponde al
    ??
    ltimo d
    ??
    gito del a
    ??
    o en curso, salvo que se trate de un pedimento consolidado iniciado en el a
    ??
    o inmediato anterior o del pedimento original de una rectificaci
    ??
    n, seguido de 6 d
    ??
    gitos de la numeraci
    ??
    n progresiva por aduana.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, NumeroPedimento=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.NumeroPedimento = _cast(None, NumeroPedimento)
        self.NumeroPedimento_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, InformacionAduaneraType4)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if InformacionAduaneraType4.subclass:
            return InformacionAduaneraType4.subclass(*args_, **kwargs_)
        else:
            return InformacionAduaneraType4(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_NumeroPedimento(self):
        return self.NumeroPedimento
    def set_NumeroPedimento(self, NumeroPedimento):
        self.NumeroPedimento = NumeroPedimento
    def validate_NumeroPedimentoType5(self, value):
        # Validate type NumeroPedimentoType5, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on NumeroPedimentoType5' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NumeroPedimentoType5_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NumeroPedimentoType5_patterns_, ))
    validate_NumeroPedimentoType5_patterns_ = [['^([0-9]{2}  [0-9]{2}  [0-9]{4}  [0-9]{7})$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='InformacionAduaneraType4', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('InformacionAduaneraType4')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'InformacionAduaneraType4':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='InformacionAduaneraType4')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='InformacionAduaneraType4', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='InformacionAduaneraType4'):
        if self.NumeroPedimento is not None and 'NumeroPedimento' not in already_processed:
            already_processed.add('NumeroPedimento')
            outfile.write(' NumeroPedimento=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.NumeroPedimento), input_name='NumeroPedimento')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='InformacionAduaneraType4', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('NumeroPedimento', node)
        if value is not None and 'NumeroPedimento' not in already_processed:
            already_processed.add('NumeroPedimento')
            self.NumeroPedimento = value
            self.validate_NumeroPedimentoType5(self.NumeroPedimento)    # validate type NumeroPedimentoType5
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class InformacionAduaneraType4


class ImpuestosType10(GeneratedsSuper):
    """ImpuestosType10 -- Nodo condicional para expresar el resumen de los impuestos aplicables.
    TotalImpuestosRetenidos -- Atributo condicional para expresar el total de los impuestos retenidos que se desprenden de los conceptos expresados en el comprobante fiscal digital por Internet. No se permiten valores negativos. Es requerido cuando en los conceptos se registren impuestos retenidos.
    TotalImpuestosTrasladados -- Atributo condicional para expresar el total de los impuestos trasladados que se desprenden de los conceptos expresados en el comprobante fiscal digital por Internet. No se permiten valores negativos. Es requerido cuando en los conceptos se registren impuestos trasladados.
    Retenciones -- Nodo condicional para capturar los impuestos retenidos aplicables. Es requerido cuando en los conceptos se registre alg
    ??
    n impuesto retenido.
    Traslados -- Nodo condicional para capturar los impuestos trasladados aplicables. Es requerido cuando en los conceptos se registre un impuesto trasladado.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TotalImpuestosRetenidos=None, TotalImpuestosTrasladados=None, Retenciones=None, Traslados=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TotalImpuestosRetenidos = _cast(None, TotalImpuestosRetenidos)
        self.TotalImpuestosRetenidos_nsprefix_ = None
        self.TotalImpuestosTrasladados = _cast(None, TotalImpuestosTrasladados)
        self.TotalImpuestosTrasladados_nsprefix_ = None
        self.Retenciones = Retenciones
        self.Retenciones_nsprefix_ = 'cfdi'
        self.Traslados = Traslados
        self.Traslados_nsprefix_ = 'cfdi'
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ImpuestosType10)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ImpuestosType10.subclass:
            return ImpuestosType10.subclass(*args_, **kwargs_)
        else:
            return ImpuestosType10(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Retenciones(self):
        return self.Retenciones
    def set_Retenciones(self, Retenciones):
        self.Retenciones = Retenciones
    def get_Traslados(self):
        return self.Traslados
    def set_Traslados(self, Traslados):
        self.Traslados = Traslados
    def get_TotalImpuestosRetenidos(self):
        return self.TotalImpuestosRetenidos
    def set_TotalImpuestosRetenidos(self, TotalImpuestosRetenidos):
        self.TotalImpuestosRetenidos = TotalImpuestosRetenidos
    def get_TotalImpuestosTrasladados(self):
        return self.TotalImpuestosTrasladados
    def set_TotalImpuestosTrasladados(self, TotalImpuestosTrasladados):
        self.TotalImpuestosTrasladados = TotalImpuestosTrasladados
    def validate_t_Importe(self, value):
        # Validate type tdCFDI:t_Importe, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on t_Importe' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_Importe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_Importe_patterns_, ))
    validate_t_Importe_patterns_ = [['^([0-9]{1,18}(.[0-9]{1,6})?)$']]
    def _hasContent(self):
        if (
            self.Retenciones is not None or
            self.Traslados is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ImpuestosType10', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ImpuestosType10')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ImpuestosType10':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ImpuestosType10')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ImpuestosType10', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ImpuestosType10'):
        if self.TotalImpuestosRetenidos is not None and 'TotalImpuestosRetenidos' not in already_processed:
            already_processed.add('TotalImpuestosRetenidos')
            outfile.write(' TotalImpuestosRetenidos="%s"' % self.gds_format_decimal(self.TotalImpuestosRetenidos, input_name='TotalImpuestosRetenidos'))
        if self.TotalImpuestosTrasladados is not None and 'TotalImpuestosTrasladados' not in already_processed:
            already_processed.add('TotalImpuestosTrasladados')
            outfile.write(' TotalImpuestosTrasladados="%s"' % self.gds_format_decimal(self.TotalImpuestosTrasladados, input_name='TotalImpuestosTrasladados'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ImpuestosType10', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Retenciones is not None:
            namespaceprefix_ = self.Retenciones_nsprefix_ + ':' if (UseCapturedNS_ and self.Retenciones_nsprefix_) else ''
            self.Retenciones.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Retenciones', pretty_print=pretty_print)
        if self.Traslados is not None:
            namespaceprefix_ = self.Traslados_nsprefix_ + ':' if (UseCapturedNS_ and self.Traslados_nsprefix_) else ''
            self.Traslados.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Traslados', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('TotalImpuestosRetenidos', node)
        if value is not None and 'TotalImpuestosRetenidos' not in already_processed:
            already_processed.add('TotalImpuestosRetenidos')
            value = self.gds_parse_decimal(value, node, 'TotalImpuestosRetenidos')
            self.TotalImpuestosRetenidos = value
            self.validate_t_Importe(self.TotalImpuestosRetenidos)    # validate type t_Importe
        value = find_attr_value_('TotalImpuestosTrasladados', node)
        if value is not None and 'TotalImpuestosTrasladados' not in already_processed:
            already_processed.add('TotalImpuestosTrasladados')
            value = self.gds_parse_decimal(value, node, 'TotalImpuestosTrasladados')
            self.TotalImpuestosTrasladados = value
            self.validate_t_Importe(self.TotalImpuestosTrasladados)    # validate type t_Importe
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Retenciones':
            obj_ = RetencionesType11.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Retenciones = obj_
            obj_.original_tagname_ = 'Retenciones'
        elif nodeName_ == 'Traslados':
            obj_ = TrasladosType13.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Traslados = obj_
            obj_.original_tagname_ = 'Traslados'
# end class ImpuestosType10


class RetencionesType11(GeneratedsSuper):
    """RetencionesType11 -- Nodo condicional para capturar los impuestos retenidos aplicables. Es requerido cuando en los conceptos se registre alg
    ??
    n impuesto retenido.
    Retencion -- Nodo requerido para la informaci
    ??
    n detallada de una retenci
    ??
    n de impuesto espec
    ??
    fico.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Retencion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Retencion is None:
            self.Retencion = []
        else:
            self.Retencion = Retencion
        self.Retencion_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RetencionesType11)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RetencionesType11.subclass:
            return RetencionesType11.subclass(*args_, **kwargs_)
        else:
            return RetencionesType11(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Retencion(self):
        return self.Retencion
    def set_Retencion(self, Retencion):
        self.Retencion = Retencion
    def add_Retencion(self, value):
        self.Retencion.append(value)
    def insert_Retencion_at(self, index, value):
        self.Retencion.insert(index, value)
    def replace_Retencion_at(self, index, value):
        self.Retencion[index] = value
    def _hasContent(self):
        if (
            self.Retencion
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='RetencionesType11', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RetencionesType11')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RetencionesType11':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RetencionesType11')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RetencionesType11', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RetencionesType11'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='RetencionesType11', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Retencion_ in self.Retencion:
            namespaceprefix_ = self.Retencion_nsprefix_ + ':' if (UseCapturedNS_ and self.Retencion_nsprefix_) else ''
            Retencion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Retencion', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Retencion':
            obj_ = RetencionType12.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Retencion.append(obj_)
            obj_.original_tagname_ = 'Retencion'
# end class RetencionesType11


class RetencionType12(GeneratedsSuper):
    """RetencionType12 -- Nodo requerido para la informaci
    ??
    n detallada de una retenci
    ??
    n de impuesto espec
    ??
    fico.
    Impuesto -- Atributo requerido para se
    ??
    alar la clave del tipo de impuesto retenido.
    Importe -- Atributo requerido para se
    ??
    alar el monto del impuesto retenido. No se permiten valores negativos.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Impuesto=None, Importe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Impuesto = _cast(None, Impuesto)
        self.Impuesto_nsprefix_ = None
        self.Importe = _cast(None, Importe)
        self.Importe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RetencionType12)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RetencionType12.subclass:
            return RetencionType12.subclass(*args_, **kwargs_)
        else:
            return RetencionType12(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Impuesto(self):
        return self.Impuesto
    def set_Impuesto(self, Impuesto):
        self.Impuesto = Impuesto
    def get_Importe(self):
        return self.Importe
    def set_Importe(self, Importe):
        self.Importe = Importe
    def validate_c_Impuesto(self, value):
        # Validate type catCFDI:c_Impuesto, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['001', '002', '003']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_Impuesto' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_t_Importe(self, value):
        # Validate type tdCFDI:t_Importe, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on t_Importe' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_Importe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_Importe_patterns_, ))
    validate_t_Importe_patterns_ = [['^([0-9]{1,18}(.[0-9]{1,6})?)$']]
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='RetencionType12', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RetencionType12')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RetencionType12':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RetencionType12')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RetencionType12', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RetencionType12'):
        if self.Impuesto is not None and 'Impuesto' not in already_processed:
            already_processed.add('Impuesto')
            outfile.write(' Impuesto=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Impuesto), input_name='Impuesto')), ))
        if self.Importe is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            outfile.write(' Importe="%s"' % self.gds_format_decimal(self.Importe, input_name='Importe'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='RetencionType12', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Impuesto', node)
        if value is not None and 'Impuesto' not in already_processed:
            already_processed.add('Impuesto')
            self.Impuesto = value
            self.validate_c_Impuesto(self.Impuesto)    # validate type c_Impuesto
        value = find_attr_value_('Importe', node)
        if value is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            value = self.gds_parse_decimal(value, node, 'Importe')
            self.Importe = value
            self.validate_t_Importe(self.Importe)    # validate type t_Importe
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class RetencionType12


class TrasladosType13(GeneratedsSuper):
    """TrasladosType13 -- Nodo condicional para capturar los impuestos trasladados aplicables. Es requerido cuando en los conceptos se registre un impuesto trasladado.
    Traslado -- Nodo requerido para la informaci
    ??
    n detallada de un traslado de impuesto espec
    ??
    fico.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Traslado=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Traslado is None:
            self.Traslado = []
        else:
            self.Traslado = Traslado
        self.Traslado_nsprefix_ = 'cfdi'
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrasladosType13)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrasladosType13.subclass:
            return TrasladosType13.subclass(*args_, **kwargs_)
        else:
            return TrasladosType13(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Traslado(self):
        return self.Traslado
    def set_Traslado(self, Traslado):
        self.Traslado = Traslado
    def add_Traslado(self, value):
        self.Traslado.append(value)
    def insert_Traslado_at(self, index, value):
        self.Traslado.insert(index, value)
    def replace_Traslado_at(self, index, value):
        self.Traslado[index] = value
    def _hasContent(self):
        if (
            self.Traslado
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='TrasladosType13', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrasladosType13')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TrasladosType13':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrasladosType13')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrasladosType13', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TrasladosType13'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='TrasladosType13', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Traslado_ in self.Traslado:
            namespaceprefix_ = self.Traslado_nsprefix_ + ':' if (UseCapturedNS_ and self.Traslado_nsprefix_) else ''
            Traslado_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Traslado', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Traslado':
            obj_ = TrasladoType14.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Traslado.append(obj_)
            obj_.original_tagname_ = 'Traslado'
# end class TrasladosType13


class TrasladoType14(GeneratedsSuper):
    """TrasladoType14 -- Nodo requerido para la informaci
    ??
    n detallada de un traslado de impuesto espec
    ??
    fico.
    Base -- Atributo requerido para se
    ??
    alar la suma de los atributos Base de los conceptos del impuesto trasladado. No se permiten valores negativos.
    Impuesto -- Atributo requerido para se
    ??
    alar la clave del tipo de impuesto trasladado.
    TipoFactor -- Atributo requerido para se
    ??
    alar la clave del tipo de factor que se aplica a la base del impuesto.
    TasaOCuota -- Atributo condicional para se
    ??
    alar el valor de la tasa o cuota del impuesto que se traslada por los conceptos amparados en el comprobante.
    Importe -- Atributo condicional para se
    ??
    alar la suma del importe del impuesto trasladado, agrupado por impuesto, TipoFactor y TasaOCuota. No se permiten valores negativos.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Base=None, Impuesto=None, TipoFactor=None, TasaOCuota=None, Importe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Base = _cast(None, Base)
        self.Base_nsprefix_ = 'cfdi'
        self.Impuesto = _cast(None, Impuesto)
        self.Impuesto_nsprefix_ = None
        self.TipoFactor = _cast(None, TipoFactor)
        self.TipoFactor_nsprefix_ = None
        self.TasaOCuota = _cast(float, TasaOCuota)
        self.TasaOCuota_nsprefix_ = None
        self.Importe = _cast(None, Importe)
        self.Importe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrasladoType14)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrasladoType14.subclass:
            return TrasladoType14.subclass(*args_, **kwargs_)
        else:
            return TrasladoType14(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Base(self):
        return self.Base
    def set_Base(self, Base):
        self.Base = Base
    def get_Impuesto(self):
        return self.Impuesto
    def set_Impuesto(self, Impuesto):
        self.Impuesto = Impuesto
    def get_TipoFactor(self):
        return self.TipoFactor
    def set_TipoFactor(self, TipoFactor):
        self.TipoFactor = TipoFactor
    def get_TasaOCuota(self):
        return self.TasaOCuota
    def set_TasaOCuota(self, TasaOCuota):
        self.TasaOCuota = TasaOCuota
    def get_Importe(self):
        return self.Importe
    def set_Importe(self, Importe):
        self.Importe = Importe
    def validate_t_Importe(self, value):
        # Validate type tdCFDI:t_Importe, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on t_Importe' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_Importe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_Importe_patterns_, ))
    validate_t_Importe_patterns_ = [['^([0-9]{1,18}(.[0-9]{1,6})?)$']]
    def validate_c_Impuesto(self, value):
        # Validate type catCFDI:c_Impuesto, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['001', '002', '003']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_Impuesto' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_c_TipoFactor(self, value):
        # Validate type catCFDI:c_TipoFactor, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Tasa', 'Cuota', 'Exento']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on c_TipoFactor' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TasaOCuotaType15(self, value):
        # Validate type TasaOCuotaType15, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0.000000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on TasaOCuotaType15' % {"value": value, "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='TrasladoType14', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrasladoType14')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TrasladoType14':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrasladoType14')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrasladoType14', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TrasladoType14'):
        if self.Base is not None and 'Base' not in already_processed:
            already_processed.add('Base')
            outfile.write(' Base="%s"' % self.gds_format_decimal(self.Base, input_name='Base'))
        if self.Impuesto is not None and 'Impuesto' not in already_processed:
            already_processed.add('Impuesto')
            outfile.write(' Impuesto=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Impuesto), input_name='Impuesto')), ))
        if self.TipoFactor is not None and 'TipoFactor' not in already_processed:
            already_processed.add('TipoFactor')
            outfile.write(' TipoFactor=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.TipoFactor), input_name='TipoFactor')), ))
        if self.TasaOCuota is not None and 'TasaOCuota' not in already_processed:
            already_processed.add('TasaOCuota')
            outfile.write(' TasaOCuota="%s"' % self.gds_format_decimal(self.TasaOCuota, input_name='TasaOCuota'))
        if self.Importe is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            outfile.write(' Importe="%s"' % self.gds_format_decimal(self.Importe, input_name='Importe'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='TrasladoType14', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Base', node)
        if value is not None and 'Base' not in already_processed:
            already_processed.add('Base')
            value = self.gds_parse_decimal(value, node, 'Base')
            self.Base = value
            self.validate_t_Importe(self.Base)    # validate type t_Importe
        value = find_attr_value_('Impuesto', node)
        if value is not None and 'Impuesto' not in already_processed:
            already_processed.add('Impuesto')
            self.Impuesto = value
            self.validate_c_Impuesto(self.Impuesto)    # validate type c_Impuesto
        value = find_attr_value_('TipoFactor', node)
        if value is not None and 'TipoFactor' not in already_processed:
            already_processed.add('TipoFactor')
            self.TipoFactor = value
            self.validate_c_TipoFactor(self.TipoFactor)    # validate type c_TipoFactor
        value = find_attr_value_('TasaOCuota', node)
        if value is not None and 'TasaOCuota' not in already_processed:
            already_processed.add('TasaOCuota')
            value = self.gds_parse_decimal(value, node, 'TasaOCuota')
            self.TasaOCuota = value
            self.validate_TasaOCuotaType15(self.TasaOCuota)    # validate type TasaOCuotaType15
        value = find_attr_value_('Importe', node)
        if value is not None and 'Importe' not in already_processed:
            already_processed.add('Importe')
            value = self.gds_parse_decimal(value, node, 'Importe')
            self.Importe = value
            self.validate_t_Importe(self.Importe)    # validate type t_Importe
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TrasladoType14


class ComplementoType(GeneratedsSuper):
    """ComplementoType -- Nodo opcional donde se incluye el complemento Timbre Fiscal Digital de manera obligatoria y los nodos complementarios determinados por el SAT, de acuerdo con las disposiciones particulares para un sector o actividad espec
    ??
    fica.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, anytypeobjs_=None, TimbreFiscalDigital=None ,gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TimbreFiscalDigital = TimbreFiscalDigital
        self.TimbreFiscalDigital_nsprefix_ = 'tfd'
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ComplementoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ComplementoType.subclass:
            return ComplementoType.subclass(*args_, **kwargs_)
        else:
            return ComplementoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_TimbreFiscalDigital(self, TimbreFiscalDigital):
        return self.TimbreFiscalDigital
    def set_TimbreFiscalDigital(self, TimbreFiscalDigital):
        self.TimbreFiscalDigital = TimbreFiscalDigital
    def _hasContent(self):
        if (
            self.TimbreFiscalDigital is not None or
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ComplementoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ComplementoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ComplementoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ComplementoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ComplementoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ComplementoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='ComplementoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TimbreFiscalDigital is not None:
            namespaceprefix_ = self.TimbreFiscalDigital_nsprefix_ + ':' if (UseCapturedNS_ and self.TimbreFiscalDigital_nsprefix_) else ''
            self.TimbreFiscalDigital.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TimbreFiscalDigital', pretty_print=pretty_print)
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TimbreFiscalDigital':
            obj_ = TimbreFiscalDigital.factory()
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TimbreFiscalDigital = obj_
            obj_.original_tagname_ = 'TimbreFiscalDigital'
        # content_ = self.gds_build_any(child_, 'ComplementoType')
        # self.anytypeobjs_.append(content_)
# end class ComplementoType

class AddendaType(GeneratedsSuper):
    """AddendaType -- Nodo opcional para recibir las extensiones al presente formato que sean de utilidad al contribuyente. Para las reglas de uso del mismo, referirse al formato origen.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AddendaType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AddendaType.subclass:
            return AddendaType.subclass(*args_, **kwargs_)
        else:
            return AddendaType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def _hasContent(self):
        if (
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='AddendaType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AddendaType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AddendaType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AddendaType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AddendaType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AddendaType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"', name_='AddendaType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        content_ = self.gds_build_any(child_, 'AddendaType')
        self.anytypeobjs_.append(content_)
# end class AddendaType

class TimbreFiscalDigital(GeneratedsSuper):
    """TimbreFiscalDigital -- Complemento requerido para el Timbrado Fiscal Digital que da validez al Comprobante fiscal digital por Internet.
    Version -- Atributo requerido para la expresi
    ??
    n de la versi
    ??
    n del est
    ??
    ndar del Timbre Fiscal Digital
    UUID -- Atributo requerido para expresar los 36 caracteres del folio fiscal (UUID) de la transacci
    ??
    n de timbrado conforme al est
    ??
    ndar RFC 4122
    FechaTimbrado -- Atributo requerido para expresar la fecha y hora, de la generaci
    ??
    n del timbre por la certificaci
    ??
    n digital del SAT. Se expresa en la forma AAAA-MM-DDThh:mm:ss y debe corresponder con la hora de la Zona Centro del Sistema de Horario en M
    ??
    xico.
    RfcProvCertif -- Atributo requerido para expresar el RFC del proveedor de certificaci
    ??
    n de comprobantes fiscales digitales que genera el timbre fiscal digital.
    Leyenda -- Atributo opcional para registrar informaci
    ??
    n que el SAT comunique a los usuarios del CFDI.
    SelloCFD -- Atributo requerido para contener el sello digital del comprobante fiscal o del comprobante de retenciones, que se ha timbrado. El sello debe ser expresado como una cadena de texto en formato Base 64.
    NoCertificadoSAT -- Atributo requerido para expresar el n
    ??
    mero de serie del certificado del SAT usado para generar el sello digital del Timbre Fiscal Digital.
    SelloSAT -- Atributo requerido para contener el sello digital del Timbre Fiscal Digital, al que hacen referencia las reglas de la Resoluci
    ??
    n Miscel
    ??
    nea vigente. El sello debe ser expresado como una cadena de texto en formato Base 64.
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Version='1.1', UUID=None, FechaTimbrado=None, RfcProvCertif=None, Leyenda=None, SelloCFD=None, NoCertificadoSAT=None, SelloSAT=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "tfd"
        self.Version = _cast(None, Version)
        self.Version_nsprefix_ = None
        self.UUID = _cast(None, UUID)
        self.UUID_nsprefix_ = None
        self.FechaTimbrado = _cast(None, FechaTimbrado)
        self.FechaTimbrado_nsprefix_ = None
        self.RfcProvCertif = _cast(None, RfcProvCertif)
        self.RfcProvCertif_nsprefix_ = None
        self.Leyenda = _cast(None, Leyenda)
        self.Leyenda_nsprefix_ = None
        self.SelloCFD = _cast(None, SelloCFD)
        self.SelloCFD_nsprefix_ = None
        self.NoCertificadoSAT = _cast(None, NoCertificadoSAT)
        self.NoCertificadoSAT_nsprefix_ = None
        self.SelloSAT = _cast(None, SelloSAT)
        self.SelloSAT_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TimbreFiscalDigital)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TimbreFiscalDigital.subclass:
            return TimbreFiscalDigital.subclass(*args_, **kwargs_)
        else:
            return TimbreFiscalDigital(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Version(self):
        return self.Version
    def set_Version(self, Version):
        self.Version = Version
    def get_UUID(self):
        return self.UUID
    def set_UUID(self, UUID):
        self.UUID = UUID
    def get_FechaTimbrado(self):
        return self.FechaTimbrado
    def set_FechaTimbrado(self, FechaTimbrado):
        self.FechaTimbrado = FechaTimbrado
    def get_RfcProvCertif(self):
        return self.RfcProvCertif
    def set_RfcProvCertif(self, RfcProvCertif):
        self.RfcProvCertif = RfcProvCertif
    def get_Leyenda(self):
        return self.Leyenda
    def set_Leyenda(self, Leyenda):
        self.Leyenda = Leyenda
    def get_SelloCFD(self):
        return self.SelloCFD
    def set_SelloCFD(self, SelloCFD):
        self.SelloCFD = SelloCFD
    def get_NoCertificadoSAT(self):
        return self.NoCertificadoSAT
    def set_NoCertificadoSAT(self, NoCertificadoSAT):
        self.NoCertificadoSAT = NoCertificadoSAT
    def get_SelloSAT(self):
        return self.SelloSAT
    def set_SelloSAT(self, SelloSAT):
        self.SelloSAT = SelloSAT
    def validate_UUIDType(self, value):
        # Validate type UUIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 36:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on UUIDType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_UUIDType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_UUIDType_patterns_, ))
    validate_UUIDType_patterns_ = [['^([a-f0-9A-F]{8}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{12})$']]
    def validate_t_FechaH(self, value):
        # Validate type tdCFDI:t_FechaH, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (datetime_.datetime)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            if not self.gds_validate_simple_patterns(
                    self.validate_t_FechaH_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_FechaH_patterns_, ))
    validate_t_FechaH_patterns_ = [['^((20[1-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]))$']]
    def validate_t_RFC_PM(self, value):
        # Validate type tdCFDI:t_RFC_PM, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) < 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on t_RFC_PM' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_t_RFC_PM_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_t_RFC_PM_patterns_, ))
    validate_t_RFC_PM_patterns_ = [['^([A-Z&??]{3}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A])$']]
    def validate_LeyendaType(self, value):
        # Validate type LeyendaType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 150:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LeyendaType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on LeyendaType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_LeyendaType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_LeyendaType_patterns_, ))
    validate_LeyendaType_patterns_ = [['^(([A-Z]|[a-z]|[0-9]| |??|??|!|"|%|&|\'|??|-|:|;|>|=|<|@|_|,|\\{|\\}|`|~|??|??|??|??|??|??|??|??|??|??|??|??){1,150})$']]
    def validate_SelloCFDType(self, value):
        # Validate type SelloCFDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_NoCertificadoSATType(self, value):
        # Validate type NoCertificadoSATType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on NoCertificadoSATType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_NoCertificadoSATType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_NoCertificadoSATType_patterns_, ))
    validate_NoCertificadoSATType_patterns_ = [['^([0-9]{20})$']]
    def validate_SelloSATType(self, value):
        # Validate type SelloSATType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital"', name_='TimbreFiscalDigital', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TimbreFiscalDigital')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TimbreFiscalDigital':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TimbreFiscalDigital')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TimbreFiscalDigital', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TimbreFiscalDigital'):
        if self.Version is not None and 'Version' not in already_processed:
            already_processed.add('Version')
            outfile.write(' Version=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Version), input_name='Version')), ))
        if self.UUID is not None and 'UUID' not in already_processed:
            already_processed.add('UUID')
            outfile.write(' UUID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.UUID), input_name='UUID')), ))
        if self.FechaTimbrado is not None and 'FechaTimbrado' not in already_processed:
            already_processed.add('FechaTimbrado')
            # outfile.write(' FechaTimbrado="%s"' % self.gds_format_datetime(self.FechaTimbrado, input_name='FechaTimbrado'))
            outfile.write(' FechaTimbrado="%s"' % self.FechaTimbrado)
        if self.RfcProvCertif is not None and 'RfcProvCertif' not in already_processed:
            already_processed.add('RfcProvCertif')
            outfile.write(' RfcProvCertif=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.RfcProvCertif), input_name='RfcProvCertif')), ))
        if self.Leyenda is not None and 'Leyenda' not in already_processed:
            already_processed.add('Leyenda')
            outfile.write(' Leyenda=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Leyenda), input_name='Leyenda')), ))
        if self.SelloCFD is not None and 'SelloCFD' not in already_processed:
            already_processed.add('SelloCFD')
            outfile.write(' SelloCFD=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.SelloCFD), input_name='SelloCFD')), ))
        if self.NoCertificadoSAT is not None and 'NoCertificadoSAT' not in already_processed:
            already_processed.add('NoCertificadoSAT')
            outfile.write(' NoCertificadoSAT=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.NoCertificadoSAT), input_name='NoCertificadoSAT')), ))
        if self.SelloSAT is not None and 'SelloSAT' not in already_processed:
            already_processed.add('SelloSAT')
            outfile.write(' SelloSAT=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.SelloSAT), input_name='SelloSAT')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital"', name_='TimbreFiscalDigital', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Version', node)
        if value is not None and 'Version' not in already_processed:
            already_processed.add('Version')
            self.Version = value
        value = find_attr_value_('UUID', node)
        if value is not None and 'UUID' not in already_processed:
            already_processed.add('UUID')
            self.UUID = value
            self.validate_UUIDType(self.UUID)    # validate type UUIDType
        value = find_attr_value_('FechaTimbrado', node)
        if value is not None and 'FechaTimbrado' not in already_processed:
            already_processed.add('FechaTimbrado')
            try:
                self.FechaTimbrado = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (FechaTimbrado): %s' % exp)
            self.validate_t_FechaH(self.FechaTimbrado)    # validate type t_FechaH
        value = find_attr_value_('RfcProvCertif', node)
        if value is not None and 'RfcProvCertif' not in already_processed:
            already_processed.add('RfcProvCertif')
            self.RfcProvCertif = value
            self.validate_t_RFC_PM(self.RfcProvCertif)    # validate type t_RFC_PM
        value = find_attr_value_('Leyenda', node)
        if value is not None and 'Leyenda' not in already_processed:
            already_processed.add('Leyenda')
            self.Leyenda = value
            self.validate_LeyendaType(self.Leyenda)    # validate type LeyendaType
        value = find_attr_value_('SelloCFD', node)
        if value is not None and 'SelloCFD' not in already_processed:
            already_processed.add('SelloCFD')
            self.SelloCFD = value
            self.validate_SelloCFDType(self.SelloCFD)    # validate type SelloCFDType
        value = find_attr_value_('NoCertificadoSAT', node)
        if value is not None and 'NoCertificadoSAT' not in already_processed:
            already_processed.add('NoCertificadoSAT')
            self.NoCertificadoSAT = value
            self.validate_NoCertificadoSATType(self.NoCertificadoSAT)    # validate type NoCertificadoSATType
        value = find_attr_value_('SelloSAT', node)
        if value is not None and 'SelloSAT' not in already_processed:
            already_processed.add('SelloSAT')
            self.SelloSAT = value
            self.validate_SelloSATType(self.SelloSAT)    # validate type SelloSATType
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TimbreFiscalDigital

GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Comprobante'
        rootClass = Comprobante
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Comprobante'
        rootClass = Comprobante
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Comprobante'
        rootClass = Comprobante
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:cfdi="http://www.sat.gob.mx/cfd/4"')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Comprobante'
        rootClass = Comprobante
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from CFDI40 import *\n\n')
        sys.stdout.write('import CFDI40 as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.sat.gob.mx/cfd/4': [],
 'http://www.sat.gob.mx/sitio_internet/cfd/catalogos': [('c_FormaPago',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Moneda',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_TipoDeComprobante',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Exportacion',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_MetodoPago',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_CodigoPostal',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Periodicidad',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Meses',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_TipoRelacion',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_RegimenFiscal',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Pais',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_UsoCFDI',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_ClaveProdServ',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_ClaveUnidad',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_ObjetoImp',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Impuesto',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_TipoFactor',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Estado',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Colonia',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Localidad',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST'),
                                                        ('c_Municipio',
                                                         'http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd',
                                                         'ST')],
 'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI': [('t_CURP',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_Importe',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_Fecha',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_ImporteMXN',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_CuentaBancaria',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_RFC',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_RFC_PM',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_RFC_PF',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_FechaHora',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_FechaH',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_Descrip100',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_NumeroDomicilio',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_Referencia',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_Descrip120',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST'),
                                                               ('t_TipoCambio',
                                                                'http://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd',
                                                                'ST')]}

__all__ = [
    "ACuentaTercerosType",
    "AddendaType",
    "CfdiRelacionadoType",
    "CfdiRelacionadosType",
    "ComplementoConceptoType",
    "ComplementoType",
    "Comprobante",
    "ConceptoType",
    "ConceptosType",
    "CuentaPredialType",
    "EmisorType",
    "ImpuestosType",
    "ImpuestosType10",
    "InformacionAduaneraType",
    "InformacionAduaneraType4",
    "InformacionGlobalType",
    "ParteType",
    "ReceptorType",
    "RetencionType",
    "RetencionType12",
    "RetencionesType",
    "RetencionesType11",
    "TrasladoType",
    "TrasladoType14",
    "TrasladosType",
    "TrasladosType13",
    "TimbreFiscalDigital",
]
