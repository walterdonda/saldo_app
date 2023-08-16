from odoo import models,api
from datetime import datetime

class ReportDetalleMovimiento(models.AbstractModel):
    _name = 'report.saldo_app.report_detalle_movimiento'
    
    @api.model
    def _get_report_values(self, docids, data=None):
        
        docs = self.env["saldo_app.movimiento"].browse(docids)
        formatted_date = datetime.now().strftime('%Y-%m-%d')  # Formatea la fecha como "YYYY-MM-DD"
        docsargs={
            "docs": docs,
            "fecha": formatted_date,
        }

        return docsargs

    
    