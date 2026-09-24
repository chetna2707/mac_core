module mac_core (
    input wire clk,
    input wire rst_n,
    input wire enable,
    input wire [7:0] a_in,
    input wire [7:0] b_in,
    output reg [19:0] accum_out
);
    reg [15:0] mult_reg;

    // Stage 1: Pipelined Multiplier
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            mult_reg <= 16'd0;
        end else if (enable) begin
            mult_reg <= a_in * b_in;
        end
    end

    // Stage 2: Accumulator
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            accum_out <= 20'd0;
        end else if (enable) begin
            accum_out <= accum_out + {{4{1'b0}}, mult_reg};
        end
    end
endmodule

