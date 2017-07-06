# -*- coding: utf-8 -*-
import StringIO
import xlwt
from django.http import HttpResponse


def get_excel_response(name, titles, rows, column_widths=None, **style):
    """   edit by xbwangh 2016-12-7
    公共接口： 获取导出Excel的response对象，利用该对象可直接在浏览器实现下载功能
    *******************************注意问题******************************
    *   1, 参数titles存放在字典data中,该参数是Excel列表头,只接受list数组    *
    *   2, name是生成Excel的文件名称                                     *
    *   3, rows是Excel数据行，只接受数组方式                              *
    *   4, 该导出方式只针对于单个sheet的excel                             *
    *   5, 如果需要修改excel样式，只需将样式参数放置于style字典中即可        *
    *               Example Param Value :                              *
    *               name = eg_name                                     *
    *               titles = ['titleA', 'titleB', 'titleC']            *
    *               rows = [['rowA1', 'rowA2','rowA3'],                *
    *                       ['rowB1', 'rowB2','rowB3'],                *
    *                       ['rowC1', 'rowC2','rowC3']                 *
    *                      ]                                           *
    *               column_widths = [20, 50, 40, 0]                    *
    *               style={'horz_align':'HORZ_CENTER'}                 *
    *   6, 列宽如果想使用默认值, 则设置为0即可                             *
    ********************************************************************
    """
    # 需要注意的是：参数rows titles必须是list类型，否则抛出异常
    if isinstance(titles, list) is False:
        raise Exception('Error Data Format : Error Format Of Param Column Title')
    if isinstance(rows, list) is False:
        raise Exception('Error Data Format : Error Format Of Param Row Data')
    # 名称非空校验
    if name is None:
        raise Exception('None Param : Param Excel Name Is None')
    # 如果列宽不为空，则必须是list类型
    if column_widths is not None and isinstance(column_widths, list) is False:
        raise Exception('Error Data Format : Error Format Of Param ColumnWidths Data')
    param_horz_alignment = style.get('horz_align')
    horizen_aligments = ['HORZ_GENERAL', 'HORZ_LEFT', 'HORZ_CENTER', 'HORZ_RIGHT', 'HORZ_FILLED',
                         'HORZ_JUSTIFIED', 'HORZ_CENTER_ACROSS_SEL', 'HORZ_DISTRIBUTED']
    if param_horz_alignment is not None and param_horz_alignment not in horizen_aligments:
        raise Exception('Error Data Format : Param style.horz_align Is Not In Specify Value')
    # 这里响应对象获得了一个特殊的content_type类型, 告诉浏览器这是个excel文件不是html
    response = HttpResponse(content_type='application/vnd.ms-excel')
    # 这里响应对象获得了附加的Content-Disposition协议头,它含有excel文件的名称,文件名随意,
    # 当浏览器访问它时,会以"另存为"对话框中使用它.
    response['Content-Disposition'] = 'attachment;filename={0}.xls'.format(name)
    # 设置Excel编码为utf-8
    wb = xlwt.Workbook(encoding='utf-8')
    # 默认情况下，Excel只有一个sheet，如果有多个，依次添加即可
    sheet = wb.add_sheet('sheet1')
    if column_widths is not None:
        for index, width in enumerate(column_widths):
            # width = 256*20  256为衡量单位，20表示20个字符宽度
            # width如果设置为0则使用默认宽度
            if width != 0:
                sheet.col(index).width = 256 * width
    # 设置对齐样式，默认居中对齐
    alignment = xlwt.Alignment()
    # 水平居中
    alignment.horz = xlwt.Alignment.HORZ_CENTER if param_horz_alignment is None else param_horz_alignment
    style = xlwt.XFStyle()
    style.alignment = alignment
    # 向excel中写入行标题
    for index, title in enumerate(titles):
        sheet.write(0, index, title, style)
    # 向Excel中写入行数据
    for i, row in enumerate(rows):
        for j, column in enumerate(row):
            sheet.write(i + 1, j, column, style)
    output = StringIO.StringIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response