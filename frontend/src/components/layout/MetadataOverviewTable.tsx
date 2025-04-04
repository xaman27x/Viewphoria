import { Card, CardContent } from "../ui/card";

const tempData = {
  file_count: 32,
  total_size: 2103,
  record_count: 1000,
  columns: [
    {
      name: "year",
      datatype: "Integer",
      description: "Yearwise revenue from icecream sales",
    },
    {
      name: "revenue",
      datatype: "Float",
      description: "revenue for the year icecream",
    },
    {
      name: "top_seller",
      datatype: "String",
      description: "Top selling product for the year",
    },
  ],
};
export default function MetadataOverviewTable() {
  return (
    <Card className="bg-transparent mb-12 text-white w-full mx-auto max-w-3xl shadow-lg rounded-2xl items-center align-middle text-center">
      <CardContent className="p-6">
        <div className="flex justify-around text-center">
          <div>
            <p className="text-xl font-semibold">{tempData.file_count}</p>
            <p className="text-md">File Count</p>
          </div>
          <div>
            <p className="text-2xl font-bold">{tempData.total_size}MB</p>
            <p className="text-md">Total Size</p>
          </div>
          <div>
            <p className="text-xl font-semibold">{tempData.record_count}</p>
            <p className="text-md">Record Count</p>
          </div>
        </div>

        <div className="mt-4 border-t border-white/40">
          <div className="grid grid-cols-3 text-sm mt-2">
            <p className="font-medium">Column Name</p>
            <p className="font-medium">Data Type</p>
            <p className="font-medium">Description</p>
          </div>

          {/* Table Rows */}
          {tempData.columns.map((col, index) => (
            <div
              key={index}
              className="grid grid-cols-3 text-sm mt-2 border-b border-white/28 py-2"
            >
              <p>{col.name}</p>
              <p>{col.datatype}</p>
              <p>{col.description}</p>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
